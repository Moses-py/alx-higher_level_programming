#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - function that returns the data of PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *string_val = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	string_val = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string_val);
}
/**
 * print_python_bytes - function that transfers data of PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bulk_size = 0, i = 0;
	char *string_val = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bulk_size = PyBytes_Size(p);
	printf("  size: %zd\n", bulk_size);
	string_val = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string_val: %s\n", string_val);
	printf("  first %zd bytes:", bulk_size < 10 ? bulk_size + 1 : 10);
	while (i < bulk_size + 1 && i < 10)
	{
		printf(" %02hhx", string_val[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - function that transfers data of PyBytesObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t bulk_size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		bulk_size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", bulk_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < bulk_size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

