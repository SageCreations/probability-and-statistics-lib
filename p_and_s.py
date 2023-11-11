import math as m

# Chapter 1 Functions

# Chapter 2 Functions

# Chapter 3 Functions

# Chapter 4 Functions

# Chapter 5 Functions

# Chapter 6 Functions ---------------------------------------------------------

def standard_normal_distribution(mu, sigma):
    return "figure this out"

# -----------------------------------------------------------------------------

# Chapter 7 Functions ---------------------------------------------------------

# How to calculate mean population with lower and upper bounds
def population_mean(a, b):
    return ((a + b) / 2)

# How to calculate the standard deviation with lower and upper bounds
def population_standard_deviation(a, b):
    return m.sqrt(m.pow(b - a, 2) / 12)

# Standard error function for chapter 7
def standard_error(sigma, n):
    return sigma / m.sqrt(n)

# The Central Limit Theorem for Sample Means (Averages)
def clt_z_score_average(xbar, mu, sigma, n):
    return ((xbar - mu) / standard_error(sigma, n))

# The Central Limit Theorem for Sums
def clt_z_score_sum(set_x, mu, sigma, n):
    return (summation(set_x) - (n * mu) / (m.sqrt(n) * sigma))

# look into distribution and invNorm calculations

# -----------------------------------------------------------------------------

# Chapter 8 Functions ---------------------------------------------------------

# 8.1 A single population mean using the normal distribution.

# Confidence Interval
def confidence_interval(xbar, ebm):
    return sub(xbar, ebm), add(xbar, ebm)

# Get z-score from somewhere else because I still don't get how it works,
# same when using alpha/2.

# Error Bound Mean
def ebm(z, se):
    return mul(z, se)

# sample size with ebm
def sample_size_ebm(z, sigma, ebm):
    return (( m.pow(z, 2) * m.pow(sigma, 2) ) / m.pow(ebm, 2))


# 8.2 A single population mean using student t distribution

# t-score
def students_t_dist(xbar, mu, s, n):
    return ( div(xbar - mu), div(s, m.sqrt(n)) )

# degrees of freedom
def simple_df(n):
    return n - 1

# 8.3 A population proportion

# sample size with ebp
def sample_size_ebp(z):
    return 'a'

# -----------------------------------------------------------------------------

# Chapter 9 Functions ---------------------------------------------------------






# -----------------------------------------------------------------------------

# Chapter 10 Functions

# Chapter 11 Functions --------------------------------------------------------

# -----------------------------------------------------------------------------

# Extras ----------------------------------------------------------------------

# add function
def add(a, b):
    return a + b

# subtract function
def sub(a, b):
    return a - b

# multiply function
def mul(a, b):
    return a * b

# divide function
def div(a, b):
    return a / b

# summation
def summation(set_x):
    sum = 0
    for i in range(0, len(set_x)+1):
        sum = sum + i

    return sum



# sample mean
def sample_mean(set_x, n):
    return summation(set_x) / n



# standard deviation
def standard_deviation():
    return "figure this out."
    
# basic z-score
def z_score(x, mu, sigma):
    return (x - mu) / sigma

# -----------------------------------------------------------------------------
