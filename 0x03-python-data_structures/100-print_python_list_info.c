#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to PyObject
 */

void print_python_list_info(PyObject *p)
{
	int len = PyList_Size(p), i;
	object = (PyListObject *)p;

	printf("[*] Size of the Python list = %d\n", len);
	printf("[*] Allocated = %d\n", object->allocated);
	for (i = 0; i < len; i++)
		printf("Element %d: %s\n", i, "str");
}
