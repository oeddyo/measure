"""
This simple script takes two files, your_prediction.txt and your_label.txt, then compute the desired measurements
"""
__author__ = 'exie'
import sys

class Measure:
    def __init__(self, pred_file, label_file):
        try:
            self.pred = [line.split()[0] for line in open(pred_file).readlines()]
            self.label = [line.split()[0] for line in open(label_file).readlines()]
        except Exception as e:
            print str("Mal-formated input. Check input")

        assert len(self.pred) == len(self.label), "One data source is longer"

        self.all_possible_classes = sorted(list(set(self.pred).union(set(self.label))))
        self.class_map = dict((x, y) for x, y in zip(self.all_possible_classes, range(len(self.all_possible_classes))))

        self.n_class = len(self.all_possible_classes)
        self._confusion_matrix()

        print "Number of class => ", self.n_class

    def _confusion_matrix(self):
        self.confusion = [[0 for x in range(self.n_class)] for x in range(self.n_class)]

        # X -> prediction
        # Y -> actual class label
        # http://en.wikipedia.org/wiki/Confusion_matrix
        for (p, l) in zip(self.pred, self.label):
            p_idx = self.class_map[p]
            l_idx = self.class_map[l]
            self.confusion[l_idx][p_idx] += 1
        return self.confusion

    def precision(self):
        self.precision_array = []
        for c in range(self.n_class):
            column_sum = sum([s[c] for s in self.confusion])
            self.precision_array.append(self.confusion[c][c]*1.0/column_sum)
        return self.precision_array

    def recall(self):
        self.recall_array = []
        for c in range(self.n_class):
            row_sum = sum(self.confusion[c])
            self.recall_array.append(self.confusion[c][c]*1.0/row_sum)

        return self.recall_array

    def F1(self):
        self.f1_array = []
        for (r, p) in zip(self.recall(), self.precision()):
            if p+r == 0.0:
                self.f1_array.append(-1.0)
            else:
                self.f1_array.append(2.0*p*r/(p+r) )
        return self.f1_array

    def __str__(self):
        self.F1()

        whole = "{0:15} {1:<8} {2:<8} {3:<8}".format("Class Name", "F1", "Pre", "Rec") + '\n'
        for c in range(self.n_class):
            output_str = "{0:15} {1:<8.4f} {2:<8.4} {3:<8.4}".format(self.all_possible_classes[c], self.f1_array[c], self.precision_array[c], self.recall_array[c])
            whole += output_str + '\n'

        return whole

if __name__ == "__main__":
    prediction_file = sys.argv[1]
    label_file = sys.argv[2]
    measure = Measure(prediction_file, label_file)
    measure.F1()
    print measure

