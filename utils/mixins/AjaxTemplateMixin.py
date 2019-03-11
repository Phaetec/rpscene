class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            if not hasattr(self, 'ajax_template_name'):
                split = self.template_name.split('.html')
                split[-1] = '_inner'
                split.append('.html')
                self.ajax_template_name = ''.join(split)
            self.template_name = self.ajax_template_name

        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)
