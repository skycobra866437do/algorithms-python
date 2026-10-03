"""General-purpose helpers for algorithm implementations."""

from typing import Callable, Iterable, Iterator, MutableSequence, Optional, Sequence, Tuple, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def swap(items: MutableSequence[T], first: int, second: int) -> None:
    """Swap two elements in a mutable sequence in place.

    Args:
        items: Mutable sequence containing the elements.
        first: Index of the first element.
        second: Index of the second element.

    Raises:
        IndexError: If either index is outside the sequence.
    """
    items[first], items[second] = items[second], items[first]


def is_sorted(
    items: Iterable[T],
    *,
    key: Optional[Callable[[T], K]] = None,
    reverse: bool = False,
) -> bool:
    """Return whether an iterable is ordered monotonically.

    Args:
        items: Values to inspect.
        key: Optional function used to extract comparison keys.
        reverse: Check descending order when true; ascending order otherwise.

    Returns:
        True when every adjacent pair is in the requested order.
        Empty and single-item iterables are considered sorted.
    """
    iterator = iter(items)
    try:
        previous_item = next(iterator)
    except StopIteration:
        return True

    previous = key(previous_item) if key is not None else previous_item
    for item in iterator:
        current = key(item) if key is not None else item
        if reverse:
            if previous < current:  # type: ignore[operator]
                return False
        elif previous > current:  # type: ignore[operator]
            return False
        previous = current

    return True


def binary_search(items: Sequence[T], target: T) -> int:
    """Find a target in an ascending sorted sequence using binary search.

    Args:
        items: Sequence sorted in ascending order.
        target: Value to locate.

    Returns:
        The index of the first matching value, or -1 when no match exists.
    """
    low = 0
    high = len(items)

    while low < high:
        middle = low + (high - low) // 2
        if items[middle] < target:  # type: ignore[operator]
            low = middle + 1
        else:
            high = middle

    if low < len(items) and items[low] == target:
        return low
    return -1


def chunked(items: Iterable[T], size: int) -> Iterator[Tuple[T, ...]]:
    """Yield values from an iterable in fixed-size chunks.

    Args:
        items: Values to divide into chunks.
        size: Maximum number of values in each chunk.

    Yields:
        Tuples containing up to ``size`` values. The final tuple may be shorter.

    Raises:
        ValueError: If ``size`` is not positive.
    """
    if size <= 0:
        raise ValueError("size must be greater than zero")

    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk.clear()

    if chunk:
        yield tuple(chunk)