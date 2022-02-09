# mmcd_to_csv

Convert CDC Multiple Mortality Cause-of-Death files to CSV format


A Python module and command line tool for converting [CDC Multiple Mortality Cause-of-Death files](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm) to CSV format.

### Example

```bash
$ mmcd_to_csv.py test_data.txt out.csv
```

Converts the mortality records in `test_data.txt` (a random sampling of 100 records from the 2020 reporting file) to `out.csv`.


### Alternate field mappings

By default, the program assumes the fields in the MMCD file are as specified in the [2020 reporting year documentation](https://www.cdc.gov/nchs/data/dvs/Multiple-Cause-Record-Layout-2020.pdf).  You can parse with other field layouts by using the `--fields_csv` option to provide a CSV specifying the mapping betwen field names and positions in the MMCD file. Positions are zero-indexed like typical Python slices. See the included file `field_specs/fields_2020.csv` for an example of how the default mapping is specified.

## Credit

Field names were derived from the code at https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser), and field positions were manually edited to conform to the 2020 specification. 