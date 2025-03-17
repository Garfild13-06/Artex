class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ControlCenter':
            return 'control_center_db'
        elif model._meta.app_label == 'LoyalityManagement':
            return 'loyality_management_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ControlCenter':
            return 'control_center_db'
        elif model._meta.app_label == 'LoyalityManagement':
            return 'loyality_management_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'ControlCenter':
            return db == 'control_center_db'
        elif app_label == 'LoyalityManagement':
            return db == 'loyality_management_db'
        return None
