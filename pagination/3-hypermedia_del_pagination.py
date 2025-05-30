#!/usr/bin/env python3
"""
Data
"""
import csv
import math
from typing import List, Dict


class Server:
    """
    Mor dat
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Data more
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        More data
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Data
        """
        assert isinstance(index, int), "index must be an integer"
        assert index >= 0, "index must be greater than or equal to 0"

        dataset = self.indexed_dataset()

        data = []
        current_index = index
        next_index = current_index + 1

        while len(data) < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }
