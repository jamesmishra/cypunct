#include <Python.h>
#define UCS4_MAX 1114111

int
shouldFilter(PyUnicodeObject* input, PySetObject* bannedSet)
{
  /*
  if (input == 32U) {
    return 1;
  }]

  return 0;
  */
  /*
  return Py_UNICODE_ISSPACE(input);
  */
  return PySet_Contains(bannedSet, input);
}

int
shouldFilterFast(Py_UCS4 input)
{
  if (input == 32U) {
    return 1;
  }
  return 0;
}

static PyObject*
cpunct_split(PyObject* self, PyObject* args)
{
  PyObject* inputStr;
  Py_ssize_t inputStrLength;
  void* inputStrData;
  int inputStrKind;
  PySetObject* bannedSet;
  PyObject* list = PyList_New(0);
  if (list == NULL) {
    return NULL;
  }
  if (!PyArg_ParseTuple(args, "UO", &inputStr, &bannedSet)) {
    return NULL;
  }
  inputStrLength = PyUnicode_GET_LENGTH(inputStr);
  inputStrData = PyUnicode_DATA(inputStr);
  inputStrKind = PyUnicode_KIND(inputStr);
  Py_ssize_t start_i = 0;
  for (Py_ssize_t i = 0; i < inputStrLength; ++i) {
    // Py_UCS4 inputChar = PyUnicode_READ(inputStrKind, inputStrData, i);
    // if (shouldFilterFast(inputChar)) {
    PyObject* inputChar = PyUnicode_Substring(inputStr, i, i + 1);
    if (shouldFilter(inputChar, bannedSet)) {
      if (start_i != i) {
        PyObject* appendSubstring = PyUnicode_Substring(inputStr, start_i, i);
        if (PyList_Append(list, appendSubstring)) {
          return NULL;
        }
      }
      start_i = i + 1;
    }
  }
  PyObject* lastAppend = PyUnicode_Substring(inputStr, start_i, inputStrLength);
  if (PyList_Append(list, lastAppend)) {
    return NULL;
  }
  return list;
}

static PyMethodDef CpunctMethods[] = {
  { "split", cpunct_split, METH_VARARGS, "Test" },
  { NULL, NULL, 0, NULL }
};

static struct PyModuleDef cpunctmodule = { PyModuleDef_HEAD_INIT,
                                           "cpunct",
                                           NULL, // module documentation
                                           -1,

                                           CpunctMethods };

PyMODINIT_FUNC
PyInit_cpunct(void)
{
  return PyModule_Create(&cpunctmodule);
}