import random
import re
import json
import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)