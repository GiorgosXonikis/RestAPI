from django.urls import path
from .views import (UserProfileView,
                    UserProfilesView,
                    UsersView,
                    UserFollowersView,
                    UserFriendsView,
                    UserUnfriendView,
                    UserFollowingView,
                    FriendRequestView,
                    FriendRequestsView,
                    FriendRequestAcceptView,
                    FriendRequestRejectView,
                    FriendRequestsPendingView)


urlpatterns = [
    path('', UsersView.as_view(), name='user-view'),
    path('<int:pk>/', UserProfileView.as_view(), name='user-profile-view'),
    path('profiles/', UserProfilesView.as_view(), name='user-profiles-view'),
    path('followers/', UserFollowersView.as_view(), name='user-followers'),
    path('friends/', UserFriendsView.as_view(), name='user-friends'),
    path('friends/unfriend/<int:user_id>/', UserUnfriendView.as_view(), name='unfriend-user'),
    path('follow/<int:user_id>/', UserFollowingView.as_view(), name='follow-user'),
    path('friendrequest/<int:user_id>/', FriendRequestView.as_view(), name='friend-request-user'),
    path('friendrequests/', FriendRequestsView.as_view(), name='friend-requests'),
    path('friendrequest/accept/<int:user_id>/', FriendRequestAcceptView.as_view(), name='friend-request-accept'),
    path('friendrequest/reject/<int:user_id>/', FriendRequestRejectView.as_view(), name='friend-requests-reject'),
    path('friendrequests/pending/', FriendRequestsPendingView.as_view(), name='friend-requests-pending'),

]