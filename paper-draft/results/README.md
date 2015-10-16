Here is the directory organization
(update every time you make changes)

|-- 2015-10-15
|   |-- K20
|   |   `-- singleGPU
|   |       |-- cusparse
|   |       |-- globalmem
|   |       `-- templated
|   `-- K40
|       `-- singleGPU
|           |-- cusparse
|           |-- globalmem
|           `-- templated
`-- README.md



2010-10-15
----------
These are results from
commit cab70d91d864f3369.

cusparse: CUSPARSE's dgtsvStridedBatch
globalmem: Precomputed cyclic reduction using only global memory
templated: Cyclic reduction on shared memory, with a template being
    used to generate kernels

