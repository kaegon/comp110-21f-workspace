"""Utility functions."""

__author__ = "730401999"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    "Prodcue a list[str] of all values in a single column."
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oreinted table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(whole: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """A function used to select a N number of rows from a table."""
    result: dict[str, list[str]] = {}
    for x in whole:
        y = []
        for z in whole[x]:
            y.append(z)
            if len(y) == n:
                break   
        result[x] = y
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """A function to select certain columns from a table into a new table."""
    result: dict[str, list[str]] = {}
    for x in table:
        if x in columns:
            result[x] = table[x]
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """A function that combines two column form tables of data."""
    end: dict[str, list[str]] = {}
    for x in one: 
        end[x] = one[x]
    for x in two:
        if x in end:
            for y in two[x]:
                end[x].append(y)
        else:
            end[x] = two[x]
    return end


def count(val: list[str]) -> dict[str, int]:
    """A function to count the frequencies of a certain data point in a set."""
    result: dict[str, int] = {}
    for x in val:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result