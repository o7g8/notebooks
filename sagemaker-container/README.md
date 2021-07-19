# SageMaker Inference endpoint hosting DifferentialMLTF2

Open `notebook/build-and-deploy.ipynb` and follow instructions there.

Stop after section `Execution inferences` and test your new endpoint as prescribed.

## TODO

- Create a GPU-enabled container.

- Compare performance of GPU- and CPU-based endpoints. Marry one of the stress-test tools <https://github.com/denji/awesome-http-benchmark> with SM Endpoint Client:

  - <https://github.com/rogerwelin/cassowary>

  - <https://www.softwaretestinghelp.com/performance-testing-tools-load-testing-tools/#6_Apache_JMeter>
