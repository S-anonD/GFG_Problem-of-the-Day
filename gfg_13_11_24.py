# 13/11/24
# Intersection Point in Y Shaped Linked Lists

def intersetPoint(head1,head2):
    ptr1 = head1
    ptr2 = head2

    if not ptr1 or not ptr2:
        return None

    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

    return ptr1.data