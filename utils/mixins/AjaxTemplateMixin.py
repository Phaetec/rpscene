from django.http import JsonResponse


class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            if not hasattr(self, 'ajax_template_name'):
                split = self.template_name.split('.html')
                split[-1] = '_inner'
                split.append('.html')
                self.ajax_template_name = ''.join(split)
            self.template_name = self.ajax_template_name

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            return JsonResponse({"id": self.object.id})
        else:
            return response
