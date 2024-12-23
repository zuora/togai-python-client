# coding: utf-8

# flake8: noqa
"""
    Togai Apis

    APIs for Togai App

    The version of the OpenAPI document: 1.0
    Contact: engg@togai.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from togai_client.models.account import Account
from togai_client.models.account_alias import AccountAlias
from togai_client.models.account_aliases import AccountAliases
from togai_client.models.account_aliases_paginated_response import AccountAliasesPaginatedResponse
from togai_client.models.account_paginated_response import AccountPaginatedResponse
from togai_client.models.account_schedule import AccountSchedule
from togai_client.models.accounts_billing_information import AccountsBillingInformation
from togai_client.models.activate_price_plan_request import ActivatePricePlanRequest
from togai_client.models.add_account_aliases_request import AddAccountAliasesRequest
from togai_client.models.add_on import AddOn
from togai_client.models.add_on_paginated_response import AddOnPaginatedResponse
from togai_client.models.add_on_type import AddOnType
from togai_client.models.address import Address
from togai_client.models.alert import Alert
from togai_client.models.alert_status import AlertStatus
from togai_client.models.alert_template import AlertTemplate
from togai_client.models.alert_templates_paginated_response import AlertTemplatesPaginatedResponse
from togai_client.models.alerts_paginated_response import AlertsPaginatedResponse
from togai_client.models.alias import Alias
from togai_client.models.alias_paginated_response import AliasPaginatedResponse
from togai_client.models.association_config import AssociationConfig
from togai_client.models.attribute import Attribute
from togai_client.models.base_success_response import BaseSuccessResponse
from togai_client.models.billing_config import BillingConfig
from togai_client.models.billing_entitlement_rate_card import BillingEntitlementRateCard
from togai_client.models.billing_entitlement_revenue_summary import BillingEntitlementRevenueSummary
from togai_client.models.bulk_rate_card_operations_request import BulkRateCardOperationsRequest
from togai_client.models.bulk_rate_card_operations_response import BulkRateCardOperationsResponse
from togai_client.models.calculate_revenue_request import CalculateRevenueRequest
from togai_client.models.calculate_revenue_response import CalculateRevenueResponse
from togai_client.models.calculate_revenue_response_v2 import CalculateRevenueResponseV2
from togai_client.models.computation import Computation
from togai_client.models.create_account_alias_request import CreateAccountAliasRequest
from togai_client.models.create_account_request import CreateAccountRequest
from togai_client.models.create_account_request_without_customer_id import CreateAccountRequestWithoutCustomerId
from togai_client.models.create_add_on_request import CreateAddOnRequest
from togai_client.models.create_alert_request import CreateAlertRequest
from togai_client.models.create_alias_request import CreateAliasRequest
from togai_client.models.create_bulk_alias_request import CreateBulkAliasRequest
from togai_client.models.create_credit_request import CreateCreditRequest
from togai_client.models.create_credit_response import CreateCreditResponse
from togai_client.models.create_custom_invoice_request import CreateCustomInvoiceRequest
from togai_client.models.create_customer_contact_request import CreateCustomerContactRequest
from togai_client.models.create_customer_contact_response import CreateCustomerContactResponse
from togai_client.models.create_customer_request import CreateCustomerRequest
from togai_client.models.create_customer_response import CreateCustomerResponse
from togai_client.models.create_entity_setting import CreateEntitySetting
from togai_client.models.create_event_schema_request import CreateEventSchemaRequest
from togai_client.models.create_feature_request import CreateFeatureRequest
from togai_client.models.create_invoice_group_request import CreateInvoiceGroupRequest
from togai_client.models.create_payment_request import CreatePaymentRequest
from togai_client.models.create_price_plan_details import CreatePricePlanDetails
from togai_client.models.create_price_plan_details_override import CreatePricePlanDetailsOverride
from togai_client.models.create_price_plan_migration_request import CreatePricePlanMigrationRequest
from togai_client.models.create_price_plan_request import CreatePricePlanRequest
from togai_client.models.create_price_plan_v2_request import CreatePricePlanV2Request
from togai_client.models.create_pricing_rule import CreatePricingRule
from togai_client.models.create_proposal_request import CreateProposalRequest
from togai_client.models.create_purchase_request import CreatePurchaseRequest
from togai_client.models.create_usage_meter_request import CreateUsageMeterRequest
from togai_client.models.credit import Credit
from togai_client.models.credit_balance_response import CreditBalanceResponse
from togai_client.models.credit_details_response import CreditDetailsResponse
from togai_client.models.credit_grant_rate_card import CreditGrantRateCard
from togai_client.models.credit_grant_revenue_summary import CreditGrantRevenueSummary
from togai_client.models.credit_grant_type import CreditGrantType
from togai_client.models.credit_rate_details import CreditRateDetails
from togai_client.models.credit_request import CreditRequest
from togai_client.models.credit_transaction import CreditTransaction
from togai_client.models.currency_config import CurrencyConfig
from togai_client.models.currency_rate_value import CurrencyRateValue
from togai_client.models.currency_slab_rate_detail import CurrencySlabRateDetail
from togai_client.models.custom_invoice_line_item import CustomInvoiceLineItem
from togai_client.models.customer import Customer
from togai_client.models.customer_paginated_response import CustomerPaginatedResponse
from togai_client.models.dependency import Dependency
from togai_client.models.dimensions_schema import DimensionsSchema
from togai_client.models.edit_account_schedule_request import EditAccountScheduleRequest
from togai_client.models.edit_pricing_schedule_request import EditPricingScheduleRequest
from togai_client.models.enriched_field import EnrichedField
from togai_client.models.enrichment_dependency import EnrichmentDependency
from togai_client.models.enrichments import Enrichments
from togai_client.models.entitlement_overage_config import EntitlementOverageConfig
from togai_client.models.entitlement_overage_config_lookup_cycle import EntitlementOverageConfigLookupCycle
from togai_client.models.entitlement_overage_entry import EntitlementOverageEntry
from togai_client.models.entitlement_overage_rate_card import EntitlementOverageRateCard
from togai_client.models.entitlement_overage_revenue_summary import EntitlementOverageRevenueSummary
from togai_client.models.error_response import ErrorResponse
from togai_client.models.event import Event
from togai_client.models.event_attribute_schema import EventAttributeSchema
from togai_client.models.event_correction_info import EventCorrectionInfo
from togai_client.models.event_correction_request import EventCorrectionRequest
from togai_client.models.event_pipeline_info import EventPipelineInfo
from togai_client.models.event_pipeline_info_account import EventPipelineInfoAccount
from togai_client.models.event_pipeline_info_customer import EventPipelineInfoCustomer
from togai_client.models.event_pipeline_info_enrichments import EventPipelineInfoEnrichments
from togai_client.models.event_pipeline_info_event_schema import EventPipelineInfoEventSchema
from togai_client.models.event_pipeline_info_feature_details import EventPipelineInfoFeatureDetails
from togai_client.models.event_pipeline_info_price_plans import EventPipelineInfoPricePlans
from togai_client.models.event_pipeline_info_revenue_details import EventPipelineInfoRevenueDetails
from togai_client.models.event_pipeline_info_usage_meters import EventPipelineInfoUsageMeters
from togai_client.models.event_schema import EventSchema
from togai_client.models.event_schema_list_data import EventSchemaListData
from togai_client.models.event_schema_list_paginated_response import EventSchemaListPaginatedResponse
from togai_client.models.event_schema_versions_response import EventSchemaVersionsResponse
from togai_client.models.event_schemas_for_feature import EventSchemasForFeature
from togai_client.models.event_source import EventSource
from togai_client.models.event_with_status import EventWithStatus
from togai_client.models.event_with_status_and_event_pipeline_info import EventWithStatusAndEventPipelineInfo
from togai_client.models.events_correction_response import EventsCorrectionResponse
from togai_client.models.expiry_type import ExpiryType
from togai_client.models.external_payment_reference import ExternalPaymentReference
from togai_client.models.feature import Feature
from togai_client.models.feature_config import FeatureConfig
from togai_client.models.feature_credit_entry import FeatureCreditEntry
from togai_client.models.feature_details import FeatureDetails
from togai_client.models.feature_list_response import FeatureListResponse
from togai_client.models.feature_paginated_list_data import FeaturePaginatedListData
from togai_client.models.file_download_url_response import FileDownloadUrlResponse
from togai_client.models.finalize_account_schedules import FinalizeAccountSchedules
from togai_client.models.finalize_price_plan_request import FinalizePricePlanRequest
from togai_client.models.fixed_fee_rate_card import FixedFeeRateCard
from togai_client.models.fixed_fee_revenue_summary import FixedFeeRevenueSummary
from togai_client.models.fixed_fee_type import FixedFeeType
from togai_client.models.get_customer_portal_delegate_token_request import GetCustomerPortalDelegateTokenRequest
from togai_client.models.get_entitlement_values_response import GetEntitlementValuesResponse
from togai_client.models.get_entitlement_values_response_data_inner import GetEntitlementValuesResponseDataInner
from togai_client.models.get_event_response import GetEventResponse
from togai_client.models.get_events_response import GetEventsResponse
from togai_client.models.get_feature_credit_entries_paginated_response import GetFeatureCreditEntriesPaginatedResponse
from togai_client.models.get_feature_credits_response import GetFeatureCreditsResponse
from togai_client.models.get_job_response import GetJobResponse
from togai_client.models.get_license_updates_response import GetLicenseUpdatesResponse
from togai_client.models.get_metrics_request import GetMetricsRequest
from togai_client.models.get_metrics_response import GetMetricsResponse
from togai_client.models.get_proposal_response import GetProposalResponse
from togai_client.models.get_purchase_response import GetPurchaseResponse
from togai_client.models.grant_details import GrantDetails
from togai_client.models.incident import Incident
from togai_client.models.incidents_paginated_response import IncidentsPaginatedResponse
from togai_client.models.ingest_batch_event_request import IngestBatchEventRequest
from togai_client.models.ingest_event_request import IngestEventRequest
from togai_client.models.ingest_event_response import IngestEventResponse
from togai_client.models.ingestion_status import IngestionStatus
from togai_client.models.invoice import Invoice
from togai_client.models.invoice_details import InvoiceDetails
from togai_client.models.invoice_details_account import InvoiceDetailsAccount
from togai_client.models.invoice_details_customer import InvoiceDetailsCustomer
from togai_client.models.invoice_details_invoice_group import InvoiceDetailsInvoiceGroup
from togai_client.models.invoice_details_organization import InvoiceDetailsOrganization
from togai_client.models.invoice_group_accounts_paginated_response import InvoiceGroupAccountsPaginatedResponse
from togai_client.models.invoice_group_details import InvoiceGroupDetails
from togai_client.models.invoice_group_paginated_response import InvoiceGroupPaginatedResponse
from togai_client.models.invoice_groups import InvoiceGroups
from togai_client.models.invoice_info_inner import InvoiceInfoInner
from togai_client.models.invoice_line_item import InvoiceLineItem
from togai_client.models.invoice_summary import InvoiceSummary
from togai_client.models.invoice_timing import InvoiceTiming
from togai_client.models.invoices_class import InvoicesClass
from togai_client.models.invoices_status import InvoicesStatus
from togai_client.models.invoices_type import InvoicesType
from togai_client.models.job_entries_paginated_response import JobEntriesPaginatedResponse
from togai_client.models.job_entries_response import JobEntriesResponse
from togai_client.models.jobs_paginated_response import JobsPaginatedResponse
from togai_client.models.jobs_without_status_info_response import JobsWithoutStatusInfoResponse
from togai_client.models.license_entries_config import LicenseEntriesConfig
from togai_client.models.license_entries_config_lookup_cycle import LicenseEntriesConfigLookupCycle
from togai_client.models.license_entries_config_lookup_range import LicenseEntriesConfigLookupRange
from togai_client.models.license_entry import LicenseEntry
from togai_client.models.license_entry_details_update_request import LicenseEntryDetailsUpdateRequest
from togai_client.models.license_rate_card import LicenseRateCard
from togai_client.models.license_rate_card_config import LicenseRateCardConfig
from togai_client.models.license_update import LicenseUpdate
from togai_client.models.license_update_request import LicenseUpdateRequest
from togai_client.models.license_update_response import LicenseUpdateResponse
from togai_client.models.list_credits_response import ListCreditsResponse
from togai_client.models.list_invoices_response import ListInvoicesResponse
from togai_client.models.list_payment_response import ListPaymentResponse
from togai_client.models.manage_miscellaneous_charges_request import ManageMiscellaneousChargesRequest
from togai_client.models.max_quantity_breach_action import MaxQuantityBreachAction
from togai_client.models.metric_data_points import MetricDataPoints
from togai_client.models.metric_data_points_grouped_by import MetricDataPointsGroupedBy
from togai_client.models.metric_name import MetricName
from togai_client.models.metric_query import MetricQuery
from togai_client.models.metric_query_filter_entry import MetricQueryFilterEntry
from togai_client.models.metric_query_response import MetricQueryResponse
from togai_client.models.migration_mode import MigrationMode
from togai_client.models.minimum_commitment import MinimumCommitment
from togai_client.models.miscellaneous_charge import MiscellaneousCharge
from togai_client.models.miscellaneous_charges_response import MiscellaneousChargesResponse
from togai_client.models.model_field import ModelField
from togai_client.models.named_license_entries_config import NamedLicenseEntriesConfig
from togai_client.models.named_license_entries_config_lookup_cycle import NamedLicenseEntriesConfigLookupCycle
from togai_client.models.named_license_entries_config_lookup_range import NamedLicenseEntriesConfigLookupRange
from togai_client.models.named_license_entry import NamedLicenseEntry
from togai_client.models.named_license_update import NamedLicenseUpdate
from togai_client.models.named_license_updates_paginated_response import NamedLicenseUpdatesPaginatedResponse
from togai_client.models.pagination_options import PaginationOptions
from togai_client.models.payment import Payment
from togai_client.models.payment_line_item_record import PaymentLineItemRecord
from togai_client.models.plan_override import PlanOverride
from togai_client.models.pre_action import PreAction
from togai_client.models.price_plan import PricePlan
from togai_client.models.price_plan_details import PricePlanDetails
from togai_client.models.price_plan_details_config import PricePlanDetailsConfig
from togai_client.models.price_plan_details_override import PricePlanDetailsOverride
from togai_client.models.price_plan_info import PricePlanInfo
from togai_client.models.price_plan_list_data import PricePlanListData
from togai_client.models.price_plan_migration_config import PricePlanMigrationConfig
from togai_client.models.price_plan_paginated_response import PricePlanPaginatedResponse
from togai_client.models.price_plan_type import PricePlanType
from togai_client.models.price_plan_v2 import PricePlanV2
from togai_client.models.price_plan_v2_paginated_response import PricePlanV2PaginatedResponse
from togai_client.models.price_type import PriceType
from togai_client.models.pricing_cycle_config import PricingCycleConfig
from togai_client.models.pricing_cycle_config_start_offset import PricingCycleConfigStartOffset
from togai_client.models.pricing_cycle_interval import PricingCycleInterval
from togai_client.models.pricing_model import PricingModel
from togai_client.models.pricing_rule import PricingRule
from togai_client.models.pricing_rule_action import PricingRuleAction
from togai_client.models.pricing_rule_changes_log import PricingRuleChangesLog
from togai_client.models.pricing_rule_info import PricingRuleInfo
from togai_client.models.pricing_rule_timing import PricingRuleTiming
from togai_client.models.pricing_rules_log import PricingRulesLog
from togai_client.models.pricing_rules_logs_paginated_response import PricingRulesLogsPaginatedResponse
from togai_client.models.pricing_rules_paginated_response import PricingRulesPaginatedResponse
from togai_client.models.pricing_rules_values import PricingRulesValues
from togai_client.models.pricing_schedule import PricingSchedule
from togai_client.models.pricing_schedule_paginated_response import PricingSchedulePaginatedResponse
from togai_client.models.pricing_schedule_with_price_plan_id import PricingScheduleWithPricePlanId
from togai_client.models.proposal import Proposal
from togai_client.models.proposals_list_response import ProposalsListResponse
from togai_client.models.proposals_paginated_response import ProposalsPaginatedResponse
from togai_client.models.prorated_refund_mode import ProratedRefundMode
from togai_client.models.proration_config import ProrationConfig
from togai_client.models.proration_config_custom_config import ProrationConfigCustomConfig
from togai_client.models.proration_config_lookup_cycle_config import ProrationConfigLookupCycleConfig
from togai_client.models.purchase import Purchase
from togai_client.models.purchase_feature_details import PurchaseFeatureDetails
from togai_client.models.purchase_list_response import PurchaseListResponse
from togai_client.models.purchase_paginated_list_data import PurchasePaginatedListData
from togai_client.models.purchase_plan_override import PurchasePlanOverride
from togai_client.models.purchase_status import PurchaseStatus
from togai_client.models.purchase_type import PurchaseType
from togai_client.models.query_column import QueryColumn
from togai_client.models.query_filter import QueryFilter
from togai_client.models.query_function import QueryFunction
from togai_client.models.query_input import QueryInput
from togai_client.models.query_input_sort_inner import QueryInputSortInner
from togai_client.models.rate_card import RateCard
from togai_client.models.rate_card_data import RateCardData
from togai_client.models.rate_card_details import RateCardDetails
from togai_client.models.rate_card_operation import RateCardOperation
from togai_client.models.rate_card_paginated_response import RateCardPaginatedResponse
from togai_client.models.rate_card_type import RateCardType
from togai_client.models.rate_plan import RatePlan
from togai_client.models.rate_value import RateValue
from togai_client.models.recurrence_config import RecurrenceConfig
from togai_client.models.remove_account_alias_request import RemoveAccountAliasRequest
from togai_client.models.remove_account_aliases_request import RemoveAccountAliasesRequest
from togai_client.models.report import Report
from togai_client.models.report_status import ReportStatus
from togai_client.models.report_type import ReportType
from togai_client.models.reports_paginated_response import ReportsPaginatedResponse
from togai_client.models.revenue_info import RevenueInfo
from togai_client.models.revenue_info_v2 import RevenueInfoV2
from togai_client.models.revenue_summary_with_metadata import RevenueSummaryWithMetadata
from togai_client.models.schedule_info import ScheduleInfo
from togai_client.models.schedules_paginated_response import SchedulesPaginatedResponse
from togai_client.models.setting import Setting
from togai_client.models.setting_data_type import SettingDataType
from togai_client.models.setting_paginated_response import SettingPaginatedResponse
from togai_client.models.slab import Slab
from togai_client.models.slab_detail import SlabDetail
from togai_client.models.slab_rate import SlabRate
from togai_client.models.slab_revenue import SlabRevenue
from togai_client.models.slab_revenue_metadata import SlabRevenueMetadata
from togai_client.models.slab_revenue_summary import SlabRevenueSummary
from togai_client.models.slab_revenue_with_metadata import SlabRevenueWithMetadata
from togai_client.models.token_response import TokenResponse
from togai_client.models.topup_wallet_request import TopupWalletRequest
from togai_client.models.update_account_request import UpdateAccountRequest
from togai_client.models.update_account_schedule_v2_request import UpdateAccountScheduleV2Request
from togai_client.models.update_add_on_request import UpdateAddOnRequest
from togai_client.models.update_alert_request import UpdateAlertRequest
from togai_client.models.update_customer_request import UpdateCustomerRequest
from togai_client.models.update_event_schema_request import UpdateEventSchemaRequest
from togai_client.models.update_feature_credits_request import UpdateFeatureCreditsRequest
from togai_client.models.update_feature_request import UpdateFeatureRequest
from togai_client.models.update_incident_status_request import UpdateIncidentStatusRequest
from togai_client.models.update_invoice_group_accounts import UpdateInvoiceGroupAccounts
from togai_client.models.update_invoice_request import UpdateInvoiceRequest
from togai_client.models.update_price_plan_request import UpdatePricePlanRequest
from togai_client.models.update_price_plan_v2_request import UpdatePricePlanV2Request
from togai_client.models.update_pricing_rules_request import UpdatePricingRulesRequest
from togai_client.models.update_pricing_schedule_request import UpdatePricingScheduleRequest
from togai_client.models.update_pricing_schedule_request_with_actions import UpdatePricingScheduleRequestWithActions
from togai_client.models.update_pricing_schedule_response import UpdatePricingScheduleResponse
from togai_client.models.update_proposal_status import UpdateProposalStatus
from togai_client.models.update_setting_request import UpdateSettingRequest
from togai_client.models.update_usage_meter_request import UpdateUsageMeterRequest
from togai_client.models.update_wallet_request import UpdateWalletRequest
from togai_client.models.usage_config import UsageConfig
from togai_client.models.usage_config_lookup_cycle import UsageConfigLookupCycle
from togai_client.models.usage_config_lookup_range import UsageConfigLookupRange
from togai_client.models.usage_cycle_interval import UsageCycleInterval
from togai_client.models.usage_lookup_range import UsageLookupRange
from togai_client.models.usage_meter import UsageMeter
from togai_client.models.usage_meter_aggregation import UsageMeterAggregation
from togai_client.models.usage_meter_filter_entry import UsageMeterFilterEntry
from togai_client.models.usage_meter_paginated_response import UsageMeterPaginatedResponse
from togai_client.models.usage_rate_card import UsageRateCard
from togai_client.models.validate_entitlement_value_request import ValidateEntitlementValueRequest
from togai_client.models.validated_entity_error import ValidatedEntityError
from togai_client.models.validated_entity_errors_paginated_response import ValidatedEntityErrorsPaginatedResponse
from togai_client.models.versions_to_migrate import VersionsToMigrate
from togai_client.models.wallet_balance_response import WalletBalanceResponse
from togai_client.models.wallet_entries_paginated_response import WalletEntriesPaginatedResponse
from togai_client.models.wallet_entry import WalletEntry
from togai_client.models.wallet_status import WalletStatus
from togai_client.models.wallet_topup_details import WalletTopupDetails
