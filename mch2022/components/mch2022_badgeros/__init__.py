import esphome.codegen as cg
import esphome.config_validation as cv

CODEOWNERS = ["@SqyD"]
DEPENDENCIES = ["wifi"]

CONF_USE_BADGEROS_WIFI = "use_badgeros_wifi"

CONF_MCH20222_BADGEROS = "mch2022_badgeros"

mch2022_badgeros_ns = cg.esphome_ns.namespace("mch2022_badgeros")

Mch2022_BadgerosComponent = mch2022_badgeros_ns.class_("Mch2022_BadgerosComponent", cg.Component)

CONFIG_SCHEMA = (
    .extend({cv.Optional(CONF_USE_BADGEROS_WIFI, default=True): cv.boolean,})
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.use_badgeros_wifi(config[CONF_USE_BADGEROS_WIFI]))