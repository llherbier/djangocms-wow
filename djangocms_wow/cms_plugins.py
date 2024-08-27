# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class AnimationPlugin(CMSPluginBase):
    model = models.Animation
    name = _('Animation')
    render_template = 'djangocms_wow/animation.html'
    allow_children = True
    text_enabled = True
    cache = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(AnimationPlugin)


class WOWAnimationPlugin(CMSPluginBase):
    model = models.WOWAnimation
    name = _("Wow Animation")
    render_template = 'djangocms_wow/wow_animation.html'
    allow_children = True
    text_enabled = True
    cache = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(WOWAnimationPlugin)
