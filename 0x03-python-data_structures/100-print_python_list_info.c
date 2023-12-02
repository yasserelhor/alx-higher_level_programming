#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    long int p_size = PyList_Size(p);
    PyListObject *obj = (PyListObject *)p;
    printf("[*] Size of the Python List = %li\n", p_size);
    printf("[*] Allocated = %li\n", obj->allocated);
    

    for (int i = 0; i < size; i++) {
        printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
    }
}

