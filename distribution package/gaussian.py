import math
import matplotlib.pyplot as plt

class Distribution:
    def __init__(self, mu=0, sigma=1):
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.
        
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            
        """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
        """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
        
        self.data = data_list
  

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        super().__init__(mu, sigma)

    def __add__(self, other):
        """Function to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        
        return result
    
    def __repr__(self):
        """Function to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return f"mean {self.mean}, standard deviation {self.stdev}"

    
    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
      
        self.sum = sum(self.data)
        self.mean = self.sum / len(self.data)
        return self.mean
                


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        if len(self.data) < 2:
            return 0
        
        mean = self.calculate_mean()
        variance = sum([(x - mean) ** 2 for x in self.data]) / (len(self.data) - int(sample))
        standard_dev = variance ** 0.5

        return standard_dev
        

    def read_data_file(self, file_name, sample=True):
    
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        
        plt.hist(self.data, bins='auto', color='blue', alpha=0.7)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.grid(True)
        plt.show()
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        exponent = -((x - self.mean) ** 2) / (2 * self.stdev ** 2)
        pdf = (1 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(exponent)
        return pdf      

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
  
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    
    
class Binomial(Distribution):
    
    def __init__(self, prob = 0.5, size = 20):
        self.p = prob
        self.n = size
        mean = self.calculate_mean()
        stdev = self.calculate_stdev()
        super().__init__(mu=mean, sigma=stdev) 
    
    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()
        
        return result
        

    
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial
        
        """
        
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"
    
    def calculate_mean(self):
        self.mean = self.p * self.n
        return self.mean
    
    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
    
    def replace_stats_with_data(self):
            
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """       
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n

def plot_histogram(self):
    """Function to output a histogram of the instance variable data using 
    matplotlib pyplot library.
    
    Args:
        None
        
    Returns:
        None
    """

    
    plt.hist(self.data, bins='auto', color='blue', alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.grid(True)
    plt.show()
    
def pdf(self, k):
    """Probability density function calculator for the gaussian distribution.
    
    Args:
        x (float): point for calculating the probability density function
        
    
    Returns:
        float: probability density function output
    """
    
    n = self.n
    p = self.p
    
    pdf = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))
    return pdf

def plot_histogram_pdf(self):
    """Function to plot the normalized histogram of the data and a plot of the 
    probability density function along the same range
    
    Args:
        None
        
    Returns:
        list: x values for the pdf plot
        list: y values for the pdf plot
        
    """
    
    x = []
    y = []
    
    for i in range(self.n + 1):
        x.append(i)
        y.append(self.pdf(i))
    
    plt.bar(x, y)
    plt.title('Binomial Distribution')
    plt.ylabel('Probability')
    plt.xlabel('Outcome')
    
    plt.show()
    
    return x, y