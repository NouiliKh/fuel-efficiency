import matplotlib.pyplot as plt
import seaborn as sns


def plot_loss_train(history, model_name):

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
    plt.bar(*zip(*history.items()))
    plt.ylabel(ylabel)
    plt.xticks(rotation=20)
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.legend()
    plt.grid(False)
    plt.show()


class EvaluateAndCompare:

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
            plot_loss_train(item, key)
        plt.show()

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