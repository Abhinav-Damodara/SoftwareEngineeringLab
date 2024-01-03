class WaterfallModel:
    def __init__(self, requirements, design, implementation, testing, deployment, maintenance):
        self.requirements = requirements
        self.design = design
        self.implementation = implementation
        self.testing = testing
        self.deployment = deployment
        self.maintenance = maintenance

    def gather_requirements(self):
        print("Gathering requirements: {}".format(self.requirements))

    def create_design(self):
        print("Creating design: {}".format(self.design))

    def implement_system(self):
        print("Implementing system: {}".format(self.implementation))

    def perform_testing(self):
        print("Performing testing: {}".format(self.testing))

    def deploy_system(self):
        print("Deploying system: {}".format(self.deployment))

    def provide_maintenance(self):
        print("Providing maintenance: {}".format(self.maintenance))

requirements = "Define user requirements"
design = "Create system design"
implementation = "Code the system"
testing = "Test the system"
deployment = "Deploy the system"
maintenance = "Provide ongoing maintenance"


waterfall_model = WaterfallModel(requirements, design, implementation, testing, deployment, maintenance)

waterfall_model.gather_requirements()
waterfall_model.create_design()
waterfall_model.implement_system()
waterfall_model.perform_testing()
waterfall_model.deploy_system()
waterfall_model.provide_maintenance()