# SageMaker Inference endpoint hosting DifferentialMLTF2

To deploy a CPU-based endpoint open `notebook/build-and-deploy.ipynb` and follow instructions there.

Stop after section `Execution inferences` and test your new endpoint as prescribed.

## TODO

- Implement concurrent request processing on GPU.
With several workers enabled we get `Blas GEMM launch failed` error on subsequent endpoint invocations.
The error goes away with a single worker, but the GPU utilization in this case is 10%, though RAM utilization is 100%.

  - Look into NVIDIA MPS `nvidia-cuda-mps-control -d` - start it in the container.
 
  - Look into GPU (MIG):

    - <https://aws.amazon.com/blogs/containers/utilizing-nvidia-multi-instance-gpu-mig-in-amazon-ec2-p4d-instances-on-amazon-elastic-kubernetes-service-eks/>
    
    - <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>
    
    - <https://www.nvidia.com/en-us/technologies/multi-instance-gpu/>
