#!/usr/bin/python3
"""Lock Boxes.

Given `n` lockboxes numbered sequentially from `0-(n -1)`, each containing keys
to other boxes. A key opens box with the same no & some may not have boxes.
All keys are +ve integers & Box 0 is unlocked.
"""


def canUnlockAll(boxes):
    """Determine if all lockboxes can be unlocked.

    Args:
        boxes (list): List of lockboxes
    Return: True if all lockboxes can be opened, False otherwise
    """
    open_box = [0]  # Make a list of opened boxes
    no = len(boxes)
    for id, box in enumerate(boxes):  # Open each box
        for key in box:
            # Check that the key in the box qualifies
            if key < no and key != id:  # id: current open box
                open_box.append(key)  # Update open_box is so
    # print('Debug: open_box => ', list(set(open_box)), ' = [`0-(n-1)`] =>',
            #      [i for i in range(no)])
    # In the return, comapare open_box to expected value
    return list(set(open_box)) == [i for i in range(no)]
