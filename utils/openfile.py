import os
import sys
import pandas as pd
import numpy as np


def openSheeshfile(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file object
    """
    try:
        foo = open(filename, "r+")
        return foo
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


def openloggerfile(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file object
    """
    try:
        foo = open(filename, "r+")
        return foo
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


def getFileSize(filename):
    """
    Args: filename [string] name of the sheesh file
    returns file filesize
    """
    try:
        file_size = os.path.getsize(filename)
        return file_size
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


def extract_table(filename):
    """
    Args: filename [string] name of the sheesh file
    returns dataframe
    """
    try:
        data = pd.read_csv(filename, sep="\t")
        # Print headers of the dataframe
        headers = data.columns.values
        headers = headers.flatten()[1:]
        data = data.values
        data = data[:, 1:]

        # delete full column from data and headers
        # headers = np.delete(headers, 38)
        # data = np.delete(data, [38], axis=1)

        # print("chud gaya humara code")

        # Find index of 'loop' column
        # while_idx = np.where(headers == "loop")[0][0]
        # print(f"while index: {while_idx}")
        # headers[while_idx + 1] = ""

        # print(headers)
        # print(data.shape)
        # print(headers.shape)
        new_data = []
        for row in data:
            new_data.append({headers[i]: row[i] for i in range(len(headers))})
        # print(data[1])
        data = new_data
        return data
    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


def extract_cfg(filename):
    """
    Args: filename [string] name of the sheesh file
    returns dataframe
    """
    try:
        # Save line by line data as an array of strings
        data = []
        with open(filename) as f:
            for line in f:
                data.append(line.strip())

        # Convert to numpy array
        data = np.array(data)
        # for e, i in enumerate(data):
        #     print(e, i)
        return data

    except:
        # check if file exists
        if not os.path.exists(filename):
            print("ERR: File does not exists")
            FileNotFoundError()
            sys.exit(1)


if __name__ == "__main__":
    # filename = "test.txt"
    # print(getFileSize(filename))
    # print(extract_table(filename))

    filename = "./Grammer/parser_LALR1_table.tsv"
    data = extract_table(filename)

    # filename = "./Grammer/Sheesh_CFG.txt"
    # data = extract_cfg(filename)
