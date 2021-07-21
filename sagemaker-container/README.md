# SageMaker Inference endpoint hosting DifferentialMLTF2

## Running Jupyter notebooks on Cloud9

Install conda as described in <https://docs.conda.io/projects/conda/en/latest/user-guide/install/rpm-debian.html> then install Jupyter and start the notebook.

```bash
sudo /opt/conda/bin/conda install ipython jupyter
/opt/conda/bin/jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser
```

Then copy the `?token=...` part and paste into the URL line of the "Run" window (it will remain blank), then open it "full screen" in a new tab.
If you get your STS token expired, then restart the jupyter server and reopen the notebook.

## Endpoints deployment

To deploy a GPU-based endpoint open `gpu/deploy.ipynb`.

To deploy a CPU-based endpoint open `notebook/build-and-deploy.ipynb` and follow instructions there.

Stop after section `Execution inferences` and test your new endpoint as prescribed.

## TODO

- Implement concurrent request processing on GPU.
With several workers enabled we get `Blas GEMM launch failed` error on subsequent endpoint invocations.
The error goes away with a single worker, but the GPU utilization in this case is 10%, though RAM utilization is 100%.

  - Look into NVIDIA MPS `nvidia-cuda-mps-control -d` - start it in the container:

    - <https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf>
    
    - <https://howtoinstall.co/en/nvidia-cuda-mps>
    
    - <https://github.com/NVIDIA/nvidia-docker/wiki/MPS-(EXPERIMENTAL)>
    
    - <https://stackoverflow.com/questions/45724523/how-to-connect-to-nvidia-mps-server-from-a-docker-container>
 
  - Look into GPU (MIG):

    - <https://aws.amazon.com/blogs/containers/utilizing-nvidia-multi-instance-gpu-mig-in-amazon-ec2-p4d-instances-on-amazon-elastic-kubernetes-service-eks/>
    
    - <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>
    
    - <https://www.nvidia.com/en-us/technologies/multi-instance-gpu/>
