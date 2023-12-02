#include "Python.h"

/**
 * print_python_list_info - Prints information about a Python List object.
 * @p: Pointer to the PyObject representing the Python List.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	PyObject *list_item;
	const char *item_type;
	PyListObject *casted_list_object;

	casted_list_object = (PyListObject *)p;
	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %d\n", (int)casted_list_object->allocated);
	
	for (Py_ssize_t i = 0; i < list_size; i++)
	{
		list_item = PyList_GetItem(p, i);
		item_type = Py_TYPE(list_item)->tp_name;
		printf("Element %ld: %s\n", i, item_type);
	}
}
