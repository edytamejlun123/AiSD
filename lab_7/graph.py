from __future__ import annotations
from enum import Enum
from typing import Any, Optional, Dict, List


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
