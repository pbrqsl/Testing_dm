import pytest
from src import exercise_4
from src.exercise_4 import add_todo, remove_todo, remove_all, edit_todo

class TestToDos:

    @pytest.fixture
    def set_todos_mock_three_elements(self, mocker):
        todos = ['a', 'b', 'c']
        mocker.patch.object(exercise_4, 'todos', todos)

    @pytest.fixture
    def set_todos_mock_one_element(self, mocker):
        todos = ['a']
        mocker.patch.object(exercise_4, 'todos', todos)

    @pytest.fixture
    def set_todos_mock_zero_elements(self, mocker):
        todos = []
        mocker.patch.object(exercise_4, 'todos', todos)

    def test_add_todo(self, set_todos_mock_three_elements):
        add_todo('d')
        expected = ['a', 'b', 'c', 'd']
        assert exercise_4.todos == expected

    def test_add_todo2(self, set_todos_mock_three_elements):
        add_todo('e')
        expected = ['a', 'b', 'c', 'e']
        assert exercise_4.todos == expected

    def test_remove_todo_more_than_two_elements(self, set_todos_mock_three_elements):
        remove_todo(0)
        expected = ['b', 'c']
        assert exercise_4.todos == expected

    def test_remove_todo_one_elelent(self, set_todos_mock_one_element):
        remove_todo(0)
        expected = []
        assert exercise_4.todos == expected

    def test_remove_all(self, set_todos_mock_three_elements):
        remove_all()
        expected = []
        assert exercise_4.todos == expected

    def test_exception_no_more_todos(self, set_todos_mock_zero_elements):
        with pytest.raises(Exception) as exception:
            remove_todo(1)
        expected = "No more todos!"
        assert str(exception.value) == expected

    def test_exception_wrong_position(self, set_todos_mock_one_element):
        with pytest.raises(Exception) as exception:
            remove_todo(2)
        expected = "No such item number!"
        assert str(exception.value) == expected

    def test_edit_todo(self, set_todos_mock_three_elements):
        edit_todo(0, 'a1')
        expected = ['a1', 'b', 'c']
        assert exercise_4.todos == expected





