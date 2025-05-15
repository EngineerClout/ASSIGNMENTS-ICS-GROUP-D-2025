import unittest
from circular_doubly_linked_list import CircularDoublyLinkedList

class TestCircularDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = CircularDoublyLinkedList()

    def test_insert_at_end(self):
        self.dll.insert_at_end(10)
        self.dll.insert_at_end(20)
        self.assertEqual(self.dll.start_node.value, 10)
        self.assertEqual(self.dll.start_node.next_node.value, 20)
        self.assertEqual(self.dll.start_node.previous_node.value, 20)  # Circular link

    def test_insert_at_beginning(self):
        self.dll.insert_at_end(10)
        self.dll.insert_at_beginning(5)
        self.assertEqual(self.dll.start_node.value, 5)
        self.assertEqual(self.dll.start_node.next_node.value, 10)
        self.assertEqual(self.dll.start_node.previous_node.value, 10)

    def test_remove_by_value(self):
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_by_value(2)
        self.assertNotEqual(self.dll.start_node.next_node.value, 2)

    def test_remove_start_node(self):
        self.dll.insert_at_end(100)
        self.dll.insert_at_end(200)
        self.dll.remove_by_value(100)
        self.assertEqual(self.dll.start_node.value, 200)

    def test_remove_all_nodes(self):
        self.dll.insert_at_end(5)
        self.dll.remove_by_value(5)
        self.assertIsNone(self.dll.start_node)

    def test_show_list_forward_output(self):
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        # Capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.dll.show_list_forward()
        sys.stdout = sys.__stdout__
        self.assertIn("1 -> 2 -> 3", captured_output.getvalue())

    def test_show_list_backward_output(self):
        self.dll.insert_at_end(4)
        self.dll.insert_at_end(5)
        self.dll.insert_at_end(6)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.dll.show_list_backward()
        sys.stdout = sys.__stdout__
        self.assertIn("6 <- 5 <- 4", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
