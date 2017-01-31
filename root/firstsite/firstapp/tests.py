from django.test import TestCase

# Create your tests here.

from django.core.paginator import PageNotAnInteger,Paginator

objects = ['join','paul','george','ringo']
p = Paginator(objects,2)
p.count