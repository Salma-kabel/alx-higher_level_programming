#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: PyObject 
 */

void print_python_list_info(PyObject *p)
{
    size_t size, i;
    PyListObject *object;
    

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    object = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", object->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, "str:Anything");
    }
}
