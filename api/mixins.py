# import random
# from datetime import datetime
# from incident_app.models import Incident
#
#
# class IncidentMixins(object):
#     @staticmethod
#     def validate_incident_id(incident_id):
#         if Incident.objects.filter(incident_id=incident_id).exists():
#             return True
#         return False
#
#     # @staticmethod
#     def get_incident_id():
#         year = datetime.now().year
#         while True:
#             random_num = random.randrange(10000, 99999)
#             incident_id = 'RMG' + str(random_num) + str(year)
#             if not self.validate_incident_id(incident_id):
#                 return incident_id
