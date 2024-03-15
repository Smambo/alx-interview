#!/usr/bin/python3
"""
The below module determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    Params:
        boxes(list): a list of lists, which represents the
        boxes to be checked.
    Returns:
        Boolean: True if all boxes can be opened,
        otherwise False
    """

    if not boxes:
        return False

    n = len(boxes)

    checked_boxes = [False] * n
    checked_boxes[0] = True
    keys = set(boxes[0])
    unchecked_boxes = [0]

    while (unchecked_boxes):
        idx = unchecked_boxes.pop(0)

        for key in boxes[idx]:
            if 0 <= key < n and not checked_boxes[key]:
                checked_boxes[key] = True
                unchecked_boxes.append(key)
                keys.update(boxes[key])

    for i in range(n):
        if not checked_boxes[i] and i in keys:
            checked_boxes[i] = True
            unchecked_boxes.append(i)

            while unchecked_boxes:
                idx = unchecked_boxes.pop(0)
                for key in boxes[idx]:
                    if 0 <= key < n and not checked_boxes[key]:
                        checked_boxes[key] = True
                        unchecked_boxes.append(key)
                        keys.update(boxes[key])

    return (all(checked_boxes))
