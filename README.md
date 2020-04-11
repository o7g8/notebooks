# notebooks
---
**polyRegBachelier.ipynb** applies differential learning in the context of classic regression models. In the article, we explored the new ideas of twin networks and differential training, mainly in the context of deep neural networks, hinting that the methodology applies to arbitrary regression models, including classic linear regression and neural architectures of arbitrary complexity, without showing other numerical results than feedforward networks, leaving extensions for online additional material. This notebook substantiates the claim and applies the methodology to polynomial regression in the context of a basket option in a correlated Bachelier model, the same context as the first numerical example in the article. We see that, in this context too, differential training provides a  massive performance improvement, without the need for additional regularization, or hyperparameter optimization.