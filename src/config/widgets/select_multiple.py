from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.models import ModelChoiceIteratorValue
from django.contrib.auth.models import User


class UserFilteredSelectMultiple(FilteredSelectMultiple):
    def __init__(self, verbose_name, is_stacked, attrs=None, choices=()):
        super().__init__(verbose_name, is_stacked, attrs, choices)
        self.aln_labels = None

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super(UserFilteredSelectMultiple, self).create_option(name, value, label, selected, index,
                                                                            subindex=None, attrs=None)
        value = ModelChoiceIteratorValue(value, instance=name)
        user = User.objects.get(pk=value.__str__())
        g_label = generate_label(user, self.aln_labels)
        print(g_label)
        option_dict['label'] = f'{user.get_full_name()}' if not g_label else g_label
        return option_dict



def generate_label(obj: object, aln_labels: list = list):
    generated_label = ""
    if aln_labels is not None:
        for label in aln_labels:
            generated_label += f" {getattr(obj, label)} |"
    return generated_label