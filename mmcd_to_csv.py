#!/usr/bin/env python

from importlib import resources
import csv

import click


def read_fields(fields_csv_file):
    fields = []
    rdr = csv.DictReader(fields_csv_file)
    for row in rdr:
        fields.append(row)
    return fields


def parse(rawfile, field_list):
    header = [i["Field"] for i in field_list]
    rows = []
    for line in rawfile:
        rowdict = {}
        for field in field_list:
            start, end = int(field["Start"]), int(field["End"])
            rowdict[field["Field"]] = line[start:end].strip()
        rows.append(rowdict)
    return header, rows


@click.command()
@click.argument("infile", type=click.File("r"))
@click.argument("outfile", type=click.File("w"))
@click.option(
    "--fields_csv",
    type=click.Path(exists=True, dir_okay=False),
    help="a CSV file specifying the mapping betwen field names and positions in the MMCD file. Defaults to the mapping for the 2020 reporting year.",
)
def to_csv(infile, outfile, fields_csv=None):
    """Convert a MMCD to a CSV file

    INFILE is the raw MMCD file to convert.
    OUTFILE is the CSV file to be created.

    A dash ('-') can be substituted for INFILE and OUTFILE to read/write from stdin and stdout respectively.
    """

    if fields_csv:
        with open(fields_csv) as f:
            fieldlist = read_fields(f)
    else:
        fields_csv = resources.open_text("field_specs", "fields_2020.csv")
        fieldlist = read_fields(fields_csv)

    header, rows = parse(infile, fieldlist)

    csvwriter = csv.DictWriter(outfile, header)
    csvwriter.writeheader()
    csvwriter.writerows(rows)


if __name__ == "__main__":
    to_csv()
