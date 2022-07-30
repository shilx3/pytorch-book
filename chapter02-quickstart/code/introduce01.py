# -*- coding: utf-8 -*-


from __future__ import print_function
import torch as t


if __name__ == '__main__':
    # x=t.Tensor([[1,2],[3,4]])
    x = t.rand(5, 3)
    print()
    print('first {}, second {}'.format(x.size()[1], x.size(1)))
