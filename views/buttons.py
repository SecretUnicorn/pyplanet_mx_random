from pyplanet.views import TemplateView

class MXRButtons(TemplateView):
    """
    2 buttons - 1 to see ranking, 1 to get help on MX_Random
    """
    template_name = "mx_random/buttons.xml"
    def __init__(self, app):
        super().__init__(app.context.ui)

        self.app = app
        self.id = "mx_random_buttons"

        self.subscribe('mx_random_toggle', self.mx_random_toggle)
        self.subscribe('mx_random_ranking', self.mx_random_ranking)
        self.subscribe('mx_set_up', self.mx_set_up)
        self.subscribe('mx_set_down', self.mx_set_down)

    async def mx_set_up(self, player, *args, **kwargs):
        return await self.app.instance.command_manager.execute(player, "//mxrup")
    
    async def mx_set_down(self, player, *args, **kwargs):
        return await self.app.instance.command_manager.execute(player, "//mxrdown")
    
    async def mx_random_toggle(self, player, *args, **kwargs):
        return await self.app.instance.command_manager.execute(player, "//mxrtoggle")
    
    async def mx_random_ranking(self, player, *args, **kwargs):
        return await self.app.instance.command_manager.execute(player, "/mxrrank")