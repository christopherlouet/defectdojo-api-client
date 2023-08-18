import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notifications_request_auto_close_engagement_item import NotificationsRequestAutoCloseEngagementItem
from ..models.notifications_request_close_engagement_item import NotificationsRequestCloseEngagementItem
from ..models.notifications_request_code_review_item import NotificationsRequestCodeReviewItem
from ..models.notifications_request_engagement_added_item import NotificationsRequestEngagementAddedItem
from ..models.notifications_request_jira_update_item import NotificationsRequestJiraUpdateItem
from ..models.notifications_request_other_item import NotificationsRequestOtherItem
from ..models.notifications_request_product_added_item import NotificationsRequestProductAddedItem
from ..models.notifications_request_product_type_added_item import NotificationsRequestProductTypeAddedItem
from ..models.notifications_request_review_requested_item import NotificationsRequestReviewRequestedItem
from ..models.notifications_request_risk_acceptance_expiration_item import (
    NotificationsRequestRiskAcceptanceExpirationItem,
)
from ..models.notifications_request_scan_added_item import NotificationsRequestScanAddedItem
from ..models.notifications_request_sla_breach_item import NotificationsRequestSlaBreachItem
from ..models.notifications_request_stale_engagement_item import NotificationsRequestStaleEngagementItem
from ..models.notifications_request_test_added_item import NotificationsRequestTestAddedItem
from ..models.notifications_request_upcoming_engagement_item import NotificationsRequestUpcomingEngagementItem
from ..models.notifications_request_user_mentioned_item import NotificationsRequestUserMentionedItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsRequest")


@_attrs_define
class NotificationsRequest:
    """
    Attributes:
        product (Union[Unset, None, int]):
        user (Union[Unset, None, int]):
        product_type_added (Union[Unset, List[NotificationsRequestProductTypeAddedItem]]):
        product_added (Union[Unset, List[NotificationsRequestProductAddedItem]]):
        engagement_added (Union[Unset, List[NotificationsRequestEngagementAddedItem]]):
        test_added (Union[Unset, List[NotificationsRequestTestAddedItem]]):
        scan_added (Union[Unset, List[NotificationsRequestScanAddedItem]]):
        jira_update (Union[Unset, List[NotificationsRequestJiraUpdateItem]]):
        upcoming_engagement (Union[Unset, List[NotificationsRequestUpcomingEngagementItem]]):
        stale_engagement (Union[Unset, List[NotificationsRequestStaleEngagementItem]]):
        auto_close_engagement (Union[Unset, List[NotificationsRequestAutoCloseEngagementItem]]):
        close_engagement (Union[Unset, List[NotificationsRequestCloseEngagementItem]]):
        user_mentioned (Union[Unset, List[NotificationsRequestUserMentionedItem]]):
        code_review (Union[Unset, List[NotificationsRequestCodeReviewItem]]):
        review_requested (Union[Unset, List[NotificationsRequestReviewRequestedItem]]):
        other (Union[Unset, List[NotificationsRequestOtherItem]]):
        sla_breach (Union[Unset, List[NotificationsRequestSlaBreachItem]]):
        risk_acceptance_expiration (Union[Unset, List[NotificationsRequestRiskAcceptanceExpirationItem]]):
        template (Union[Unset, bool]):
    """

    product: Union[Unset, None, int] = UNSET
    user: Union[Unset, None, int] = UNSET
    product_type_added: Union[Unset, List[NotificationsRequestProductTypeAddedItem]] = UNSET
    product_added: Union[Unset, List[NotificationsRequestProductAddedItem]] = UNSET
    engagement_added: Union[Unset, List[NotificationsRequestEngagementAddedItem]] = UNSET
    test_added: Union[Unset, List[NotificationsRequestTestAddedItem]] = UNSET
    scan_added: Union[Unset, List[NotificationsRequestScanAddedItem]] = UNSET
    jira_update: Union[Unset, List[NotificationsRequestJiraUpdateItem]] = UNSET
    upcoming_engagement: Union[Unset, List[NotificationsRequestUpcomingEngagementItem]] = UNSET
    stale_engagement: Union[Unset, List[NotificationsRequestStaleEngagementItem]] = UNSET
    auto_close_engagement: Union[Unset, List[NotificationsRequestAutoCloseEngagementItem]] = UNSET
    close_engagement: Union[Unset, List[NotificationsRequestCloseEngagementItem]] = UNSET
    user_mentioned: Union[Unset, List[NotificationsRequestUserMentionedItem]] = UNSET
    code_review: Union[Unset, List[NotificationsRequestCodeReviewItem]] = UNSET
    review_requested: Union[Unset, List[NotificationsRequestReviewRequestedItem]] = UNSET
    other: Union[Unset, List[NotificationsRequestOtherItem]] = UNSET
    sla_breach: Union[Unset, List[NotificationsRequestSlaBreachItem]] = UNSET
    risk_acceptance_expiration: Union[Unset, List[NotificationsRequestRiskAcceptanceExpirationItem]] = UNSET
    template: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product = self.product
        user = self.user
        product_type_added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.product_type_added, Unset):
            product_type_added = []
            for product_type_added_item_data in self.product_type_added:
                product_type_added_item = product_type_added_item_data.value

                product_type_added.append(product_type_added_item)

        product_added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.product_added, Unset):
            product_added = []
            for product_added_item_data in self.product_added:
                product_added_item = product_added_item_data.value

                product_added.append(product_added_item)

        engagement_added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.engagement_added, Unset):
            engagement_added = []
            for engagement_added_item_data in self.engagement_added:
                engagement_added_item = engagement_added_item_data.value

                engagement_added.append(engagement_added_item)

        test_added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.test_added, Unset):
            test_added = []
            for test_added_item_data in self.test_added:
                test_added_item = test_added_item_data.value

                test_added.append(test_added_item)

        scan_added: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scan_added, Unset):
            scan_added = []
            for scan_added_item_data in self.scan_added:
                scan_added_item = scan_added_item_data.value

                scan_added.append(scan_added_item)

        jira_update: Union[Unset, List[str]] = UNSET
        if not isinstance(self.jira_update, Unset):
            jira_update = []
            for jira_update_item_data in self.jira_update:
                jira_update_item = jira_update_item_data.value

                jira_update.append(jira_update_item)

        upcoming_engagement: Union[Unset, List[str]] = UNSET
        if not isinstance(self.upcoming_engagement, Unset):
            upcoming_engagement = []
            for upcoming_engagement_item_data in self.upcoming_engagement:
                upcoming_engagement_item = upcoming_engagement_item_data.value

                upcoming_engagement.append(upcoming_engagement_item)

        stale_engagement: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stale_engagement, Unset):
            stale_engagement = []
            for stale_engagement_item_data in self.stale_engagement:
                stale_engagement_item = stale_engagement_item_data.value

                stale_engagement.append(stale_engagement_item)

        auto_close_engagement: Union[Unset, List[str]] = UNSET
        if not isinstance(self.auto_close_engagement, Unset):
            auto_close_engagement = []
            for auto_close_engagement_item_data in self.auto_close_engagement:
                auto_close_engagement_item = auto_close_engagement_item_data.value

                auto_close_engagement.append(auto_close_engagement_item)

        close_engagement: Union[Unset, List[str]] = UNSET
        if not isinstance(self.close_engagement, Unset):
            close_engagement = []
            for close_engagement_item_data in self.close_engagement:
                close_engagement_item = close_engagement_item_data.value

                close_engagement.append(close_engagement_item)

        user_mentioned: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_mentioned, Unset):
            user_mentioned = []
            for user_mentioned_item_data in self.user_mentioned:
                user_mentioned_item = user_mentioned_item_data.value

                user_mentioned.append(user_mentioned_item)

        code_review: Union[Unset, List[str]] = UNSET
        if not isinstance(self.code_review, Unset):
            code_review = []
            for code_review_item_data in self.code_review:
                code_review_item = code_review_item_data.value

                code_review.append(code_review_item)

        review_requested: Union[Unset, List[str]] = UNSET
        if not isinstance(self.review_requested, Unset):
            review_requested = []
            for review_requested_item_data in self.review_requested:
                review_requested_item = review_requested_item_data.value

                review_requested.append(review_requested_item)

        other: Union[Unset, List[str]] = UNSET
        if not isinstance(self.other, Unset):
            other = []
            for other_item_data in self.other:
                other_item = other_item_data.value

                other.append(other_item)

        sla_breach: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sla_breach, Unset):
            sla_breach = []
            for sla_breach_item_data in self.sla_breach:
                sla_breach_item = sla_breach_item_data.value

                sla_breach.append(sla_breach_item)

        risk_acceptance_expiration: Union[Unset, List[str]] = UNSET
        if not isinstance(self.risk_acceptance_expiration, Unset):
            risk_acceptance_expiration = []
            for risk_acceptance_expiration_item_data in self.risk_acceptance_expiration:
                risk_acceptance_expiration_item = risk_acceptance_expiration_item_data.value

                risk_acceptance_expiration.append(risk_acceptance_expiration_item)

        template = self.template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user
        if product_type_added is not UNSET:
            field_dict["product_type_added"] = product_type_added
        if product_added is not UNSET:
            field_dict["product_added"] = product_added
        if engagement_added is not UNSET:
            field_dict["engagement_added"] = engagement_added
        if test_added is not UNSET:
            field_dict["test_added"] = test_added
        if scan_added is not UNSET:
            field_dict["scan_added"] = scan_added
        if jira_update is not UNSET:
            field_dict["jira_update"] = jira_update
        if upcoming_engagement is not UNSET:
            field_dict["upcoming_engagement"] = upcoming_engagement
        if stale_engagement is not UNSET:
            field_dict["stale_engagement"] = stale_engagement
        if auto_close_engagement is not UNSET:
            field_dict["auto_close_engagement"] = auto_close_engagement
        if close_engagement is not UNSET:
            field_dict["close_engagement"] = close_engagement
        if user_mentioned is not UNSET:
            field_dict["user_mentioned"] = user_mentioned
        if code_review is not UNSET:
            field_dict["code_review"] = code_review
        if review_requested is not UNSET:
            field_dict["review_requested"] = review_requested
        if other is not UNSET:
            field_dict["other"] = other
        if sla_breach is not UNSET:
            field_dict["sla_breach"] = sla_breach
        if risk_acceptance_expiration is not UNSET:
            field_dict["risk_acceptance_expiration"] = risk_acceptance_expiration
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        product_type_added: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.product_type_added, Unset):
            _temp_product_type_added = []
            for product_type_added_item_data in self.product_type_added:
                product_type_added_item = product_type_added_item_data.value

                _temp_product_type_added.append(product_type_added_item)
            product_type_added = (None, json.dumps(_temp_product_type_added).encode(), "application/json")

        product_added: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.product_added, Unset):
            _temp_product_added = []
            for product_added_item_data in self.product_added:
                product_added_item = product_added_item_data.value

                _temp_product_added.append(product_added_item)
            product_added = (None, json.dumps(_temp_product_added).encode(), "application/json")

        engagement_added: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.engagement_added, Unset):
            _temp_engagement_added = []
            for engagement_added_item_data in self.engagement_added:
                engagement_added_item = engagement_added_item_data.value

                _temp_engagement_added.append(engagement_added_item)
            engagement_added = (None, json.dumps(_temp_engagement_added).encode(), "application/json")

        test_added: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.test_added, Unset):
            _temp_test_added = []
            for test_added_item_data in self.test_added:
                test_added_item = test_added_item_data.value

                _temp_test_added.append(test_added_item)
            test_added = (None, json.dumps(_temp_test_added).encode(), "application/json")

        scan_added: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.scan_added, Unset):
            _temp_scan_added = []
            for scan_added_item_data in self.scan_added:
                scan_added_item = scan_added_item_data.value

                _temp_scan_added.append(scan_added_item)
            scan_added = (None, json.dumps(_temp_scan_added).encode(), "application/json")

        jira_update: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.jira_update, Unset):
            _temp_jira_update = []
            for jira_update_item_data in self.jira_update:
                jira_update_item = jira_update_item_data.value

                _temp_jira_update.append(jira_update_item)
            jira_update = (None, json.dumps(_temp_jira_update).encode(), "application/json")

        upcoming_engagement: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.upcoming_engagement, Unset):
            _temp_upcoming_engagement = []
            for upcoming_engagement_item_data in self.upcoming_engagement:
                upcoming_engagement_item = upcoming_engagement_item_data.value

                _temp_upcoming_engagement.append(upcoming_engagement_item)
            upcoming_engagement = (None, json.dumps(_temp_upcoming_engagement).encode(), "application/json")

        stale_engagement: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.stale_engagement, Unset):
            _temp_stale_engagement = []
            for stale_engagement_item_data in self.stale_engagement:
                stale_engagement_item = stale_engagement_item_data.value

                _temp_stale_engagement.append(stale_engagement_item)
            stale_engagement = (None, json.dumps(_temp_stale_engagement).encode(), "application/json")

        auto_close_engagement: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.auto_close_engagement, Unset):
            _temp_auto_close_engagement = []
            for auto_close_engagement_item_data in self.auto_close_engagement:
                auto_close_engagement_item = auto_close_engagement_item_data.value

                _temp_auto_close_engagement.append(auto_close_engagement_item)
            auto_close_engagement = (None, json.dumps(_temp_auto_close_engagement).encode(), "application/json")

        close_engagement: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.close_engagement, Unset):
            _temp_close_engagement = []
            for close_engagement_item_data in self.close_engagement:
                close_engagement_item = close_engagement_item_data.value

                _temp_close_engagement.append(close_engagement_item)
            close_engagement = (None, json.dumps(_temp_close_engagement).encode(), "application/json")

        user_mentioned: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.user_mentioned, Unset):
            _temp_user_mentioned = []
            for user_mentioned_item_data in self.user_mentioned:
                user_mentioned_item = user_mentioned_item_data.value

                _temp_user_mentioned.append(user_mentioned_item)
            user_mentioned = (None, json.dumps(_temp_user_mentioned).encode(), "application/json")

        code_review: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.code_review, Unset):
            _temp_code_review = []
            for code_review_item_data in self.code_review:
                code_review_item = code_review_item_data.value

                _temp_code_review.append(code_review_item)
            code_review = (None, json.dumps(_temp_code_review).encode(), "application/json")

        review_requested: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.review_requested, Unset):
            _temp_review_requested = []
            for review_requested_item_data in self.review_requested:
                review_requested_item = review_requested_item_data.value

                _temp_review_requested.append(review_requested_item)
            review_requested = (None, json.dumps(_temp_review_requested).encode(), "application/json")

        other: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.other, Unset):
            _temp_other = []
            for other_item_data in self.other:
                other_item = other_item_data.value

                _temp_other.append(other_item)
            other = (None, json.dumps(_temp_other).encode(), "application/json")

        sla_breach: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.sla_breach, Unset):
            _temp_sla_breach = []
            for sla_breach_item_data in self.sla_breach:
                sla_breach_item = sla_breach_item_data.value

                _temp_sla_breach.append(sla_breach_item)
            sla_breach = (None, json.dumps(_temp_sla_breach).encode(), "application/json")

        risk_acceptance_expiration: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.risk_acceptance_expiration, Unset):
            _temp_risk_acceptance_expiration = []
            for risk_acceptance_expiration_item_data in self.risk_acceptance_expiration:
                risk_acceptance_expiration_item = risk_acceptance_expiration_item_data.value

                _temp_risk_acceptance_expiration.append(risk_acceptance_expiration_item)
            risk_acceptance_expiration = (
                None,
                json.dumps(_temp_risk_acceptance_expiration).encode(),
                "application/json",
            )

        template = (
            self.template if isinstance(self.template, Unset) else (None, str(self.template).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if user is not UNSET:
            field_dict["user"] = user
        if product_type_added is not UNSET:
            field_dict["product_type_added"] = product_type_added
        if product_added is not UNSET:
            field_dict["product_added"] = product_added
        if engagement_added is not UNSET:
            field_dict["engagement_added"] = engagement_added
        if test_added is not UNSET:
            field_dict["test_added"] = test_added
        if scan_added is not UNSET:
            field_dict["scan_added"] = scan_added
        if jira_update is not UNSET:
            field_dict["jira_update"] = jira_update
        if upcoming_engagement is not UNSET:
            field_dict["upcoming_engagement"] = upcoming_engagement
        if stale_engagement is not UNSET:
            field_dict["stale_engagement"] = stale_engagement
        if auto_close_engagement is not UNSET:
            field_dict["auto_close_engagement"] = auto_close_engagement
        if close_engagement is not UNSET:
            field_dict["close_engagement"] = close_engagement
        if user_mentioned is not UNSET:
            field_dict["user_mentioned"] = user_mentioned
        if code_review is not UNSET:
            field_dict["code_review"] = code_review
        if review_requested is not UNSET:
            field_dict["review_requested"] = review_requested
        if other is not UNSET:
            field_dict["other"] = other
        if sla_breach is not UNSET:
            field_dict["sla_breach"] = sla_breach
        if risk_acceptance_expiration is not UNSET:
            field_dict["risk_acceptance_expiration"] = risk_acceptance_expiration
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product = d.pop("product", UNSET)

        user = d.pop("user", UNSET)

        product_type_added = []
        _product_type_added = d.pop("product_type_added", UNSET)
        for product_type_added_item_data in _product_type_added or []:
            product_type_added_item = NotificationsRequestProductTypeAddedItem(product_type_added_item_data)

            product_type_added.append(product_type_added_item)

        product_added = []
        _product_added = d.pop("product_added", UNSET)
        for product_added_item_data in _product_added or []:
            product_added_item = NotificationsRequestProductAddedItem(product_added_item_data)

            product_added.append(product_added_item)

        engagement_added = []
        _engagement_added = d.pop("engagement_added", UNSET)
        for engagement_added_item_data in _engagement_added or []:
            engagement_added_item = NotificationsRequestEngagementAddedItem(engagement_added_item_data)

            engagement_added.append(engagement_added_item)

        test_added = []
        _test_added = d.pop("test_added", UNSET)
        for test_added_item_data in _test_added or []:
            test_added_item = NotificationsRequestTestAddedItem(test_added_item_data)

            test_added.append(test_added_item)

        scan_added = []
        _scan_added = d.pop("scan_added", UNSET)
        for scan_added_item_data in _scan_added or []:
            scan_added_item = NotificationsRequestScanAddedItem(scan_added_item_data)

            scan_added.append(scan_added_item)

        jira_update = []
        _jira_update = d.pop("jira_update", UNSET)
        for jira_update_item_data in _jira_update or []:
            jira_update_item = NotificationsRequestJiraUpdateItem(jira_update_item_data)

            jira_update.append(jira_update_item)

        upcoming_engagement = []
        _upcoming_engagement = d.pop("upcoming_engagement", UNSET)
        for upcoming_engagement_item_data in _upcoming_engagement or []:
            upcoming_engagement_item = NotificationsRequestUpcomingEngagementItem(upcoming_engagement_item_data)

            upcoming_engagement.append(upcoming_engagement_item)

        stale_engagement = []
        _stale_engagement = d.pop("stale_engagement", UNSET)
        for stale_engagement_item_data in _stale_engagement or []:
            stale_engagement_item = NotificationsRequestStaleEngagementItem(stale_engagement_item_data)

            stale_engagement.append(stale_engagement_item)

        auto_close_engagement = []
        _auto_close_engagement = d.pop("auto_close_engagement", UNSET)
        for auto_close_engagement_item_data in _auto_close_engagement or []:
            auto_close_engagement_item = NotificationsRequestAutoCloseEngagementItem(auto_close_engagement_item_data)

            auto_close_engagement.append(auto_close_engagement_item)

        close_engagement = []
        _close_engagement = d.pop("close_engagement", UNSET)
        for close_engagement_item_data in _close_engagement or []:
            close_engagement_item = NotificationsRequestCloseEngagementItem(close_engagement_item_data)

            close_engagement.append(close_engagement_item)

        user_mentioned = []
        _user_mentioned = d.pop("user_mentioned", UNSET)
        for user_mentioned_item_data in _user_mentioned or []:
            user_mentioned_item = NotificationsRequestUserMentionedItem(user_mentioned_item_data)

            user_mentioned.append(user_mentioned_item)

        code_review = []
        _code_review = d.pop("code_review", UNSET)
        for code_review_item_data in _code_review or []:
            code_review_item = NotificationsRequestCodeReviewItem(code_review_item_data)

            code_review.append(code_review_item)

        review_requested = []
        _review_requested = d.pop("review_requested", UNSET)
        for review_requested_item_data in _review_requested or []:
            review_requested_item = NotificationsRequestReviewRequestedItem(review_requested_item_data)

            review_requested.append(review_requested_item)

        other = []
        _other = d.pop("other", UNSET)
        for other_item_data in _other or []:
            other_item = NotificationsRequestOtherItem(other_item_data)

            other.append(other_item)

        sla_breach = []
        _sla_breach = d.pop("sla_breach", UNSET)
        for sla_breach_item_data in _sla_breach or []:
            sla_breach_item = NotificationsRequestSlaBreachItem(sla_breach_item_data)

            sla_breach.append(sla_breach_item)

        risk_acceptance_expiration = []
        _risk_acceptance_expiration = d.pop("risk_acceptance_expiration", UNSET)
        for risk_acceptance_expiration_item_data in _risk_acceptance_expiration or []:
            risk_acceptance_expiration_item = NotificationsRequestRiskAcceptanceExpirationItem(
                risk_acceptance_expiration_item_data
            )

            risk_acceptance_expiration.append(risk_acceptance_expiration_item)

        template = d.pop("template", UNSET)

        notifications_request = cls(
            product=product,
            user=user,
            product_type_added=product_type_added,
            product_added=product_added,
            engagement_added=engagement_added,
            test_added=test_added,
            scan_added=scan_added,
            jira_update=jira_update,
            upcoming_engagement=upcoming_engagement,
            stale_engagement=stale_engagement,
            auto_close_engagement=auto_close_engagement,
            close_engagement=close_engagement,
            user_mentioned=user_mentioned,
            code_review=code_review,
            review_requested=review_requested,
            other=other,
            sla_breach=sla_breach,
            risk_acceptance_expiration=risk_acceptance_expiration,
            template=template,
        )

        notifications_request.additional_properties = d
        return notifications_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
