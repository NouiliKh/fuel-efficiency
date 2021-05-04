import matplotlib.pyplot as plt


def plot_train(history, model_name):
    """
    used to plot 3 plots: loss, val_loss and execution_time for all models presented in the history dictionary.
    ...
    Attributes
    ----------
    history : dict
        dictionary presents logs of the training.
    model_name: str
        the model_name
    """
    plt.subplot(1, 3, 1)
    plt.plot(history['loss'], label=model_name)
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error loss [MPG]')
    plt.grid(True)

    plt.subplot(1, 3, 2)  # index 2
    plt.plot(history['val_loss'], label=model_name)
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error val_loss [MPG]')
    plt.grid(True)

    plt.subplot(1, 3, 3)  # index 2
    plt.plot(history['execution_time'], label=model_name)
    plt.xlabel('Epoch')
    plt.ylabel('Execution_time')
    plt.grid(True)
    plt.legend()


def plot_evaluate(history, ylabel):
    """
    used to plot a bar plot for all models presented in the history dictionary.
    ...
    Attributes
    ----------
    history : dict
        dictionary presents logs of the training.
    y_label: str
        the model_name
    """
    plt.clf()
    plt.bar(*zip(*history.items()))
    plt.ylabel(ylabel)
    plt.xticks(rotation=20)
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.legend()
    plt.grid(False)
    plt.savefig('../output/compare_' + ylabel + '.png')
    # plt.show()


class EvaluateAndCompare:
    """
     A class used to evaluate and compare between the models trained.
     ...
     Attributes
     ----------
     format string : str
         format used to print the string in elegant format
     training_data : dict
         logs of the models while training
     evaluation_data : bool
         logs of the model while evaluating

     Methods
     -------
     plots()
         Plot the log data and save the plots.
     compare()
         Compare between the models and prints some results.
     """
    def __init__(self, gathered_data):
        self.format_string = "{:<50}|{:<30}|{:<30}"
        self.training_data = {}
        self.evaluation_data = {}
        for key, item in gathered_data.items():
            if 'train' in key:
                self.training_data[key] = item
            if 'evaluate' in key:
                self.evaluation_data[key] = item

    def plots(self):
        for key, item in self.training_data.items():
            plot_train(item, key)
        plt.savefig('../output/compare1.png')
        # plt.show()

        eval_bar_plot = {}
        time_bar_plot = {}
        for key, item in self.evaluation_data.items():
            eval_bar_plot[key] = item['loss']
            time_bar_plot[key] = item['execution_time']

        plot_evaluate(eval_bar_plot, 'Loss')
        plot_evaluate(time_bar_plot, 'Execution time')

    def compare(self):
        shortest_execution_time_training = 404
        shortest_execution_time_training_model_name = 'Not found'
        shortest_execution_time_evaluating = 404
        shortest_execution_time_evaluating_model_name = 'Not found'
        loss = 404
        most_performant = 'Not found'

        header = ['Model name', 'Loss', 'Execution time']
        print('-------------------------------------------------------------------------------------------------------')

        print(self.format_string.format(*header))
        print('Training')

        for key, item in self.training_data.items():
            if shortest_execution_time_training > item['execution_time'][-1].numpy():
                shortest_execution_time_training = item['execution_time'][-1].numpy()
                shortest_execution_time_training_model_name = key
            print(self.format_string.format(*[key, item['loss'][-1], item['execution_time'][-1].numpy()]))
        print('Evaluation')

        for key, item in self.evaluation_data.items():
            if shortest_execution_time_evaluating > item['execution_time'].numpy():
                shortest_execution_time_evaluating = item['execution_time'].numpy()
                shortest_execution_time_evaluating_model_name = key

            if loss > item['loss']:
                most_performant = key
                loss = item['loss']
            print(self.format_string.format(*[key, item['loss'], item['execution_time'].numpy()]))

        print('-------------------------------------------------------------------------------------------------------')
        print('Most performant model:  ' + str(most_performant) + ' with loss ' + str(loss))
        print('fastest model while training:  ' + str(shortest_execution_time_training_model_name) + 'with execution time ' + str(shortest_execution_time_training))
        print('fastest model while testing:  ' + str(shortest_execution_time_evaluating_model_name) + 'with execution time ' + str(shortest_execution_time_evaluating))