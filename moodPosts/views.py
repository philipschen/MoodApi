from rest_framework import generics, mixins, permissions

from moodPosts.models import Moodposts
from moodPosts.serializer import MoodSerializer


class MoodPostAPIView(generics.ListCreateAPIView):
    lookup_field            = 'pk'
    serializer_class        = MoodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Moodposts.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data.append({"streak":Moodposts.objects.filter(user=self.request.user).count()})

        selfuser = Moodposts.objects.filter(user=self.request.user).values('user')[0]['user']#.first
        streaks = {}
        allPosts = Moodposts.objects.all().values('user')
        # for user in user.objects.all()
        #   count = user.user.count()
        for objects in allPosts:
            if objects['user'] not in streaks:
                streaks[objects['user']] = 1
            else:
                streaks[objects['user']] += 1
        sorted_list = sorted([(k,v) for v,k in streaks.items()])
        streakpercent = 0
        for idx,x in enumerate(sorted_list):
            if selfuser == x[1]:
                streakpercent = (idx+1)/len(sorted_list) * 100
                break
        if streakpercent >= 50:
            response.data.append({"streak_percentile": f'{streakpercent:.2f}th Percentile'})
        return response