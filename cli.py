import argparse
import numpy as np
from models import (
    PolynomialModel,
    fit_elastic_modulus,
    fit_hardness,
    larson_miller_parameter,
    oxide_thickness,
)
from export import export_csv, export_json


def parse_array(values: list[str]) -> np.ndarray:
    return np.array([float(v) for v in values])


def cmd_fit_modulus(args: argparse.Namespace) -> None:
    model = fit_elastic_modulus(parse_array(args.temperatures), parse_array(args.values), args.degree)
    coeffs = model.coeffs.tolist()
    print("coefficients:", coeffs)
    if args.out:
        export_json(args.out, {"coefficients": coeffs})


def cmd_fit_hardness(args: argparse.Namespace) -> None:
    model = fit_hardness(parse_array(args.temperatures), parse_array(args.values), args.degree)
    coeffs = model.coeffs.tolist()
    print("coefficients:", coeffs)
    if args.out:
        export_json(args.out, {"coefficients": coeffs})


def cmd_predict(args: argparse.Namespace) -> None:
    model = PolynomialModel(np.array(args.coeffs, dtype=float))
    value = model.predict(args.temperature)
    print(args.property, value)


def cmd_creep(args: argparse.Namespace) -> None:
    lmp = larson_miller_parameter(args.temperature, args.time, args.C)
    print("Larson-Miller parameter:", lmp)
    if args.out:
        export_csv(args.out, {"LMP": lmp})


def cmd_oxide(args: argparse.Namespace) -> None:
    thickness = oxide_thickness(args.kp, args.time, args.initial)
    print("Oxide thickness:", thickness)
    if args.out:
        export_csv(args.out, {"thickness": thickness})


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="CALPHAD simulation tools")
    sub = parser.add_subparsers(dest="command")

    fm = sub.add_parser("fit-modulus")
    fm.add_argument("--temperatures", nargs="+", required=True)
    fm.add_argument("--values", nargs="+", required=True)
    fm.add_argument("--degree", type=int, default=1)
    fm.add_argument("--out", help="export results to JSON")
    fm.set_defaults(func=cmd_fit_modulus)

    fh = sub.add_parser("fit-hardness")
    fh.add_argument("--temperatures", nargs="+", required=True)
    fh.add_argument("--values", nargs="+", required=True)
    fh.add_argument("--degree", type=int, default=1)
    fh.add_argument("--out", help="export results to JSON")
    fh.set_defaults(func=cmd_fit_hardness)

    pred = sub.add_parser("predict")
    pred.add_argument("property", choices=["modulus", "hardness"])
    pred.add_argument("--coeffs", nargs="+", type=float, required=True)
    pred.add_argument("--temperature", type=float, required=True)
    pred.set_defaults(func=cmd_predict)

    creep = sub.add_parser("creep-rupture")
    creep.add_argument("--temperature", type=float, required=True)
    creep.add_argument("--time", type=float, required=True, help="hours")
    creep.add_argument("--C", type=float, default=20.0)
    creep.add_argument("--out", help="export CSV")
    creep.set_defaults(func=cmd_creep)

    oxide = sub.add_parser("oxide-growth")
    oxide.add_argument("--kp", type=float, required=True)
    oxide.add_argument("--time", type=float, required=True)
    oxide.add_argument("--initial", type=float, default=0.0)
    oxide.add_argument("--out", help="export CSV")
    oxide.set_defaults(func=cmd_oxide)

    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
