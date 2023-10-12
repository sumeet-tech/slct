"""Views initialization module."""
from .alerts import AlertTransactionViewSet, CrmApprovalStageGatesViewSet
from .backhauling_viewset import (
    BackhaulingInboundTruckDropdown,
    BackhaulingInboundTruckViewSet,
    BackhaulingOpportunitiesCardsViewSet,
    BackhaulingOpportunitiesDropdown,
    BackhaulingOpportunitiesViewSet,
    BackhaulingRunView,
)
from .custom_viewsets import DownloadUploadViewSet, FileUploadViewSet
from .daily_scheduling_views import (  # LpSchedulingPlantConstraintUploadDownloadViewSet,; SourceChangeModeTotalImpact,
    BackhaulingProcessDropdownViewSet,
    ChangeSourceApprovalRequest,
    DemandBackhaulingProcessViewSet,
    DepoAdditionRunListViewSet,
    DepotAdditionOutputRunView,
    DepotAdditionOutputViewViewSet,
    GetWarehouseId,
    LpSchedulingDiDtlDropdownViewSet,
    LpSchedulingDiDtlViewSet,
    LpSchedulingOrderExecutableDropdownView,
    LpSchedulingOrderExecutableView,
    LpSchedulingOrderMasterCityDropdownView,
    LpSchedulingOrderMasterDistrictDropdownView,
    LpSchedulingOrderMasterDropdownView,
    LpSchedulingOrderMasterEditDropdownViewSet,
    LpSchedulingOrderMasterSourceChange,
    LpSchedulingOrderMasterUpdateView,
    LpSchedulingOrderMasterViewSet,
    LpSchedulingOrderNonExecutableView,
    LpSchedulingPackerConstraintDropdownView,
    LpSchedulingPackerConstraintView,
    LpSchedulingPlantConstraintDropdownView,
    LpSchedulingPlantConstraintViewSet,
    LpSchedulingPpSequenceDropdown,
    LpSchedulingPpSequenceView,
    LpSchedulingVehicleConstraintDropdownView,
    LpSchedulingVehicleConstraintView,
    LpScriptViewSet,
    OrderExecutableDetailUpdateOrCreate,
    OrderExecutableQuantitySumView,
    OrderPoolSourceChangeDropdown,
    PackerRatedCapacityDropdown,
    PackerShiftConstraintListView,
    PackerShiftConstraintViewSet,
    RouteRestrictionsViewSet,
    SourceChangeContributionDifference,
    SourceChangeFreightMasterViewSet,
    SystemRecommendationTechicalActivities,
    TaregtSettingDownload,
)
from .decision_on_negative_contribution_market_view import (
    NshContributionScenarioViewSet,
    NshScenarioAnalysisContributionData,
    TOebsSclArNcrAdvanceCalcTabDropdown,
)
from .handling_agent_views import (  # GodownDispatchViewSet,; CrossingDataViewSet,; DiversionsViewSet,; RhFiringViewSet,; SlabRangeViewSet,;
    AllproductsDropdown,
    CostMasterCostHeadViewSet,
    CostsMasterDetailViewSet,
    CrwcChargesMasterDropdown,
    CrwcChargesMasterViewSet,
    DayWiseInventory,
    DemurrageSlabsViewSet,
    DepotOperationsViewSet,
    EpodDataReachedViewSet,
    EpodDataVehicleNoAndDeliveryIdDropdown,
    EpodDataViewSet,
    FreightChangeFormatDownloadView,
    FreightChangeInitiationDropdown,
    FreightChangeInitiationStatusCountViewSet,
    FreightChangeInitiationViewSet,
    GdVsWharfageModelRunView,
    GdWharfageOutputViewSet,
    GetSlabsCode,
    GetTimeCombination,
    GodownPerformance,
    GodownTat,
    HandingAgentDashboardDropdown,
    HandlingAgentDashboard,
    HandlingMastersViewSet,
    HourlyLiftingEfficiencyMasterViewSet,
    HourlyLiftingEfficiencyViewSet,
    LiftingPatternViewSet,
    MonthlyInventory,
    MonthlyWiseInventory,
    NewFreightInitiationDropdown,
    NewFreightInitiationStatusCountViewSet,
    NewFreightInitiationViewSet,
    OrderStatusRecievedViewSet,
    OrderStatusViewSet,
    ProductWiseDropdown,
    ProductWiseInventory,
    RailExpensesDetailsViewSet,
    RailExpensesDetailsWfViewSet,
    RailRoadFlagDropdownViewSet,
    RailRoadFlagViewSet,
    ReasonForFreightChangeDropdown,
    ReasonsForDemurrageWharfageView,
    RoadRakeCoordinatorAPIView,
    SidingConstraintsCheckViewSet,
    SidingConstraintsViewSet,
    StockAvailabilityindepot,
    StockAvailabilityViewSet,
    SumOfClosingPointView,
    TgtDayWiseLiftingViewSet,
    TgtMrnDataViewSet,
    TgtPlantDispatchDataAPIView,
    TgtPlantDispatchDataDropdownAPIView,
    TgtPlantDispatchDataDropdownAPIViewnew,
    TgtPlantSiloCapacityDropdown,
    TGTPlantSiloCapacityViewSet,
    TgtRakeChargesViewSet,
    TgtRakeDisposalsViewSet,
    TgtRakeLoadingDetailDropdown,
    TgtRakeLoadingDetailsViewSet,
    TgtRakeLoadingDropdown,
    TgtRakeLoadingGetViewSet,
    TgtRakeLoadingViewSet,
    TgtRakeUnloadingDetailsViewSet,
    TgtSlhOrderPendencyQuantitySumAndCount,
    TgtSlhOrderPendencyViewSet,
    TgtSlhServiceLevelDepoAPIView,
    TgtSlhServiceLevelDepoQuantitySumAndCount,
    WaiverCommissionMasterDropdown,
    WaiverCommissionMasterViewSet,
    WaterFallChartInventoryDropdownViewSet,
    WaterfallChartInventoryViewSet,
    WharfageSlabsViewSet,
)
from .influencer_manager_view import (
    AnnualInfluencerManagerPLanLastYearAvg,
    AugmentationOutputTableDownloadAPIView,
    CreateAnnualInflncrPlnYearly,
    CreateAnnualMeetPlanYearly,
    CrmInflAssistReqDataByIdViewSet,
    CrmInflAssistReqDropdown,
    CrmInflChgReqDataByIdViewSet,
    CrmInflChgReqDropdown,
    CrmInflGiftSchemeviewset,
    CrmInflMgrAnnualPlanDownloadUploadViewset,
    CrmInflMgrAnnualPlanMonthlyViewSet,
    CrmInflMgrAnnualPlanViewSet,
    CrmInflMgrMeetPlanDownloadUploadViewset,
    CrmInflMgrMeetPlanMonthlyViewSet,
    CrmInflMgrMeetPlanViewSet,
    CrmInflMgrSchemeBudgetViewSet,
    CrmInflSchemeViewSet,
    GetCrmInflAssistReqDataViewSet,
    GetCrmInflChgReqDataViewSet,
    GetPrvYrSelectdMnthCrmAnnualPlanViewSet,
    GetPrvYrSelectdMnthMgrMeetPlanDataViewSet,
    GetStateCaseStudyDataViewSet,
    InfluencerMeetBudgetOutputAPIView,
    InfluencerMeetFreeRunInputView,
    InfluencerMeetingOutputViewSet,
    InfluencerOutputView,
    InfluencerOutputViewSet,
    InfluencerTechActivityMasterDropdown,
    InfluencerTechActivityMasterViewSet,
    LastYearMeetPlanAvg,
    LstYrBudgetAvgCrmInflMgrSchemeBudgetViewSet,
    SoAugmentationRunView,
    StateCaseStudyDataByIdViewSet,
    StateCaseStudyViewSet,
)
from .marketing_branding_views import (
    BrandingActivityDropDown,
    BrandingActivityViewSet,
    CalcTabDealerNameDropdown,
    CrmMabBrandingApprByIdViewSet,
    CrmMabBrandingApprViewSet,
    CrmMabBtlPlanningByIdViewSet,
    CrmMabBtlPlanningViewSet,
    CrmMabInitReqViewSet,
    CrmMabPastRequisitionsByIdViewSet,
    CrmMabPastRequisitionsViewSet,
    GetAllVendorsViewSet,
    GetVendorsByStateViewSet,
    MarketMappingBrandingBudgetDropDown,
    MarketMappingBrandingBudgetViewSet,
    NewMarketPricingApprovalViewSet,
    SponsorshipBudgetViewSet,
    TnmMaterialTransactionDropdown,
    VendorDetailMasterDropdown,
    VendorDetailMasterVendorCodeDropdown,
)
from .monthly_scheduling_views import (
    ClinkerALlocationAnalysis,
    ClinkerDemandRunView,
    ClinkerDispatchGUPlantDropdown,
    ClinkerLinksMasterDropDownView,
    CLinkerLinksMasterViewSet,
    DeliveryCreationView,
    DemandDropdownView,
    DemandListView,
    DispatchAPIView,
    DjpCounterScoreViewSet,
    DjpRouteScoreViewSet,
    DjpRunViewSet,
    ExportToExcelView,
    FreightBasedQuantity,
    GdWarfhageRunListView,
    GetCLinkerDemandRunDataViewSet,
    GetDemandDataByIdViewSet,
    GetLastUpdatedDate,
    GodownMasterDropdownView,
    GodownMasterListView,
    GodownMasterViewSet,
    LinksMasterDropdownView,
    LinksMasterViewSet,
    LpMinCapacityViewSet,
    LpModelDfFnlBaseListAPIView,
    LpModelDfFnlScenarioAnalysisView,
    LpModelDfFnlView,
    LpModelRunListView,
    LpModelRunUpdate,
    LpModelScenarioAnalysisExportView,
    LpTargetSettingsDropdownViewSet,
    LpTargetSettingView,
    MonthlyNthBudget,
    OrderUpdateView,
    OutputScreenDropdown,
    PackagingMasterDropdownView,
    PackagingMasterViewSet,
    PackerConstraintsMViewSet,
    PlantConstraintsMViewSet,
    PlantDispatchPlan,
    PlantDispatchPlanAnalysis,
    PlantProductMasterDropdownView,
    PlantProductsMasterViewSet,
    PpCallView,
    PriceMasterViewSet,
    RailHandlingDownView,
    RailHandlingView,
    RakeTransferDetails,
    RakeTypesDropdown,
    RoadVsRakeView,
    RouteRestrictionDropdownView,
    RouteUpdateView,
    SampleDownloadView,
    ServiceLevelSlaDropdownView,
    ServiceLevelSlaViewSet,
    SidingCodeMappingDropdown,
    StateViewSet,
    TLCBreakupView,
    TOebsSclAddressLinkDropdown,
    VehicleAvailabilityDropdownView,
    VehicleAvailabilityViewSet,
    VpcHistoricalPlantDropdown,
)
from .non_trade_views import (
    AnnualSalesTargetAccountView,
    AnnualSalesTargetNtsoKamView,
    AnnualSalesTargetProductView,
    AnnualSalesTargetStateView,
    BrandApprovalDropdownView,
    BrandApprovalViewSet,
    ConsensusTargetForNtTargetSumViewSet,
    ConsensusTargetForNtViewSet,
    CreditLimitNtChangeStatus,
    CreditLimitNtView,
    CrmNthBankGuartApprViewSet,
    CrmNthCustCodeCreViewSet,
    CrmNthExtendValidityViewSet,
    CrmNthLeadFormDropDown,
    CrmNthLeadFormViewSet,
    CrmNthOrderCancApprViewSet,
    CrmNthQuotNcrExcpApprViewSet,
    CrmNthRefuReqViewSet,
    CrmNthSoNcrExcpApprViewSet,
    CrmNthSourceChgReqViewSet,
    DimAccountNameDropdown,
    DimCustomersTestViewSet,
    DimCustomersView,
    DimPeriodMonthsDropdown,
    DimPeriodYearsDropdown,
    DimProductTestDropdown,
    DimResourceDesignationDropdown,
    DimResourceDropdown,
    DimResourcesListView,
    FactNtSalesPlanAnnualViewSet,
    FactNtSalesPlanningMonthGetPreviousMonthDataViewSet,
    FactNtSalesPlanningMonthViewSet,
    FactNtSalesPlanningNcrGetPreviousMonthDataViewSet,
    FactNtSalesPlanningNcrViewSet,
    FactNtSalesPlanningViewSet,
    GetCustomerBasedOnResource,
    MonthlyTargetSettingTargetSum,
    MonthlyTargetSettingViewSet,
    NcrCalculator,
    NcrCalculatorDropdown,
    NonTradeHeadMonthlySalesData,
    NonTradeHeadMonthlySalesDropdown,
    NonTradeSalesDropdown,
    NonTradeSalesPlanningAccountMonthlyViewSet,
    NonTradeSalesPlanningAccountViewSet,
    NonTradeSalesPlanningAdherence,
    NonTradeSalesPlanningDesignationMonthlyViewSet,
    NonTradeSalesPlanningDesignationViewSet,
    NonTradeSalesPlanningMonthlyNcrTargetViewSet,
    NonTradeSalesPlanningProductMonthlyViewSet,
    NonTradeSalesPlanningProductViewSet,
    NonTradeSalesPlanningSelectedYearSelectedMonthTotalMonthTargetsViewSet,
    NonTradeSalesPlanningSelectedYearTotalMonthTargetsViewSet,
    NonTradeSalesPlanningStateMonthlyViewSet,
    NonTradeSalesPlanningStateViewSet,
    NonTradeTopDownMonthlyTargetViewSet,
    NshNonTradeSalesActualViewSet,
    NtBottomUpAnnualCards,
    NtCommunicationView,
    NtCreditLimitDropdown,
    NTHConsensusTargetMonthlySalesPlan,
    NTHMarketPotentialAndShareMonthlyViewSet,
    NTInputSPConsensusTarget,
    NtMarketTargetBulkCreateViewSet,
    NtMonthlySalesPlanContributionData,
    NtMonthlySalesPlanNcrData,
    NtNcrMonthlySales,
    NtNcrThresholdCityDropdownView,
    NtNcrThresholdDistrictsDropdownView,
    NtNcrThresholdDropdownView,
    NtNcrThresholdView,
    NtNotesView,
    NTPremiumProductsMasterTmpDropdown,
    NtProductTargetByState,
    NtResourceTargetViewSet,
    NtSalesPlanningDesignationActuals,
    NtSalesPlanningMonthlyNCRMonthActual,
    NtSalesPlanningMonthlyQuantityHistoricalActuals,
    NTTopDownMonthProductActual,
    PremiumProductsMasterTmpBGPDropdown,
    ResourcesNameDropdown,
    SchemeProductDropdown,
    SumApi,
    SumForAnnualTargetColumnWise,
    TgtOrderDataApCustomerAndTPCDropdown,
    TgtOrderDataApTPCDropdown,
    ThreeMonthsOldCustomerData,
    TOebsHzCustAccountsView,
    TpcCustomerMappingViewSet,
    TransferAccounts,
    TransferOfficersAllAccounts,
)
from .packing_plant_views import (  # PpDowntimeEntryViewSet,; PpDowntimeViewSet,; UpdatePpDowntimeListViewSet,; SourceChangeModeTotalImpact,
    AacPlantDropdownView,
    BackUnloadingEnrouteMarketsMasterDropdownView,
    BackUnloadingEnrouteMarketsMasterViewSet,
    BagBurstDispatchQty,
    CementPlantDropdownView,
    ClinkerDispatchPlanViewSet,
    DemurrageAndWharfageForecastViewSet,
    GetAdhocQtyListViewSet,
    GetDowntimeDataViewSet,
    GetPackerRatedCapacityViewSet,
    GetPackingPlanOutputViewSet,
    GetPlantDepoSlaPlantAndProductList,
    GetStoppageDescriptionList,
    L1SourceMappingRouteIdDropdown,
    L1SourceMappingViewSet,
    LpSchedulingDpcByIdViewSet,
    LpSchedulingDpcDropdownView,
    LpSchedulingDpcViewSet,
    MvPendingReasonsForDelayDropdown,
    MvPendingReasonsForDelayViewSet,
    PackerBagBurstingDescDataByIdViewSet,
    PackerBagBurstingDescViewSet,
    PackerShiftLevelStoppagesDropdownView,
    PackerShiftLevelStoppagesMainListViewSet,
    PackerShiftLevelStoppagesViewSet,
    PackingPlantAacTatReasonsDownloadView,
    PackingPlantAacTatReasonsView,
    PackingPlantBagsStockDropdownView,
    PackingPlantBagsStockViewSet,
    PackingPlantCementTatReasonsView,
    PackingPlantScriptRunModel,
    PlantDepoSlaNewViewSet,
    PlantDepoSlaView,
    PlantStorageView,
    PpMasterViewSet,
    PpOrderTaggingDropdown,
    PpRailOrderTaggingValueViewSet,
    ShiftWiseAdhocPercentageViewSet,
    ShiftWiseAdhocQtyBulkCreateViewSet,
    ShiftWiseAdhocQtyViewSet,
    SourceChangeModeViewSet,
    TgtBridgingCostAPIView,
    TgtBridgingCostViewSet,
    TgtTruckCycleTatAacView,
    TgtTruckCycleTatCementView,
    TOebsApSuppliersViewSet,
    TOebsSclRouteMasterViewSet,
    UniqueValueViewSet,
    UpdateAdhocQtyListViewSet,
    UpdatePackerShiftLevelStoppagesListViewSet,
)
from .pricing_strategy_views import (
    CompetitionPriceNewMarketsDownloadUploadViewSet,
    CompetitionPriceNewMarketsDropdown,
    GetVpcByPlant,
    NewPriceComputationDropdown,
    NewPriceComputationGetBenchmarkViewSet,
    NewPriceComputationViewSet,
    NmMarket4X4OutputViewSet,
    NmMarketSharePotentialDropdown,
    NmMarketSharePotentialViewSet,
    PriceBenchmarksDownloadUploadViewSet,
    PriceBenchmarksDropdown,
    PriceChangeApprovalGet,
    PriceChangeReqApproval,
    PriceChangeRequestApprovalDropdown,
    PriceComputationBaseSegmentDropdown,
    PricingModelRunView,
    SoLeagueWeightageViewSet,
    VpcHistoricalDropdown,
)
from .sales_planning_views import (  # PlanDataForMonthViewSet,
    AnnualUrbanizationRateViewSet,
    AverageDepotAdditionOutputView,
    AverageFlatSizeViewSet,
    BottomUpNtViewSet,
    CementConsumptionViewSet,
    ConsensusTargetDropdownView,
    ConsensusTargetMonthlysalesplan,
    ConsensusTargetUpdateDownloadViewSet,
    ConsensusTargetViewSet,
    DemandForecastRunViewSet,
    DemandSplitMissingView,
    DemandSplitView,
    DepotAdditionMasterDropdownViewSet,
    DepotAdditionMasterViewSet,
    DepotAdditionOutputDropdownViewSet,
    DepotAdditionOutputViewSet,
    DesiredMarketShareViewSet,
    DfBottomUpTargetsMonthly2ViewSet,
    DfMacroOutputFinalViewSet,
    DistrictClassification,
    ExistingDepotLocationsViewSet,
    GeographicalPresenceViewSet,
    GetDesiredMarketShareStatesViewSet,
    GetGeographicalPresenceStatesViewSet,
    HighRiseLowRiseSplitViewSet,
    IFramesUrlMapping,
    KachaPakkaConversionRateViewSet,
    MacroAnalysisScriptRunView,
    MarketMappingBrandingOuputViewSet,
    MarketMappingChannelStrategyViewSet,
    MarketMappingCounterStrategyViewSet,
    MarketMappingDistrictClassificationViewSet,
    MarketMappingGrowthPotentialDropdown,
    MarketMappingGrowthPotentialViewSet,
    MarketMappingMarketPotentialDropdown,
    MarketMappingMarketPotentialViewSet,
    MarketMappingPricingOutputViewSet,
    MarketMappingRunRunModel,
    MarketMappingSalesTargetViewSet,
    MarketMappingStateClassificationViewSet,
    MarketPotentialAndShareMonthlyViewSet,
    ProjectDbViewSet,
    SeasonalityViewSet,
    StatesCities,
    TdtMultiplierDropdown,
    TdtMultiplierViewSet,
    TopDownTargetsDropdownView,
    TopDownTargetsViewSet,
    UrbanRuralHouseholdSizeViewSet,
)
from .scheme_view import (
    CreateCrmComplaintsViewSet,
    CrmComplaintsDropdown,
    CrmComplaintsViewSet,
    GetCrmComplaintsByIdViewSet,
    GetStateSchemeByIdViewSet,
    GetStateSchemeViewSet,
    GiftMasterDropdown,
    SchemeViewSet,
)
from .state_head_views import (  # SlctCashDiscPropsByIdViewSet,
    ActivityBudgetExpenseAPI,
    AnnualDistrictLevelTargetDropdown,
    AnnualDistrictLevelTargetViewSet,
    AnnualStateLevelTargetCommentAndStatus,
    AnnualStateLevelTargetDropdown,
    AnnualStateLevelTargetViewSet,
    AutomatedModelsRunStatusView,
    CrmExceptionApprovalForReplacementOfProductDropdown,
    CrmExceptionApprovalForReplacementOfProductViewset,
    CrmMarketMappingPricingDropdown,
    CrmMarketMappingPricingViewSet,
    CrmPricingViewSet,
    CrmSalesPlanAndAdherenceViewset,
    CrmSalesPlanningBottomUpTargetSum,
    CrmSalesPlanningBottomUpTargetViewset,
    CrmVerificationAndApprovalOfDealerSpFormViewSet,
    DistrictWisePricingProposalViewSet,
    ExceptionDisbursementApprovalDropdown,
    ExceptionDisbursementApprovalViewSet,
    GiftRedeemRequestApprovalDropdown,
    GiftRedeemRequestApprovalViewSet,
    NetworkAdditionCardsData,
    NetworkAdditionPlanStateSendToNshButtonViewSet,
    NetworkAdditionPlanStateViewSet,
    NetworkAdditionPlanViewSet,
    NetworkAdditionStateCardsData,
    PlantDepoMasterDropdownView,
    PricingInputCrmPricingListViewSet,
    RevisedBucketsApprovalDropdown,
    SalesPlanApproval,
    SHAnnualStateLevelTargetApprovalCards,
    SlctActivityPropsByIdViewSet,
    SlctActivityPropsViewSet,
    SlctAnnualDiscSlabBasedByIdViewSet,
    SlctAnnualDiscSlabBasedViewSet,
    SlctAnnualDiscTargetBasedByIdViewSet,
    SlctAnnualDiscTargetBasedViewSet,
    SlctAnnualSalesPlanByIdViewSet,
    SlctAnnualSalesPlanDownloadViewSet,
    SlctAnnualSalesPlanViewSet,
    SlctBenchmarkChangeRequestByIdViewSet,
    SlctBenchmarkChangeRequestViewSet,
    SlctBoosterPerDayGrowthSchemeByIdViewSet,
    SlctBoosterPerDayGrowthSchemeViewSet,
    SlctBoosterPerDayTargetSchemeByIdViewSet,
    SlctBoosterPerDayTargetSchemeViewSet,
    SlctBorderDiscPropsByIdViewSet,
    SlctBorderDiscPropsViewSet,
    SlctBrandingRequestsByIdViewSet,
    SlctBrandingRequestsViewSet,
    SlctCashDiscPropsByIDViewSet,
    SlctCashDiscPropsViewSet,
    SlctCombSlabGrowthPropsByIdViewSet,
    SlctCombSlabGrowthPropsViewSet,
    SlctDealerLinkedSchPropsByIdViewSet,
    SlctDealerLinkedSchPropsViewSet,
    SlctDealerOutsBasedPropsByIdViewSet,
    SlctDealerOutsBasedPropsViewSet,
    SlctDirPltBilngDiscPropsByIdViewSet,
    SlctDirPltBilngDiscPropsViewSet,
    SlctDownloadExcel,
    SlctEngCashSchPtPropsByIdViewSet,
    SlctEngCashSchPtPropsViewSet,
    SlctGapWithOtherProductByIdViewSet,
    SlctInKindBoosterSchemePropsByIdViewSet,
    SlctInKindBoosterSchemePropsViewSet,
    SlctInKindTourProposalByIdViewSet,
    SlctInKindTourProposalViewSet,
    SlctMasonKindSchPropsByIdViewSet,
    SlctMasonKindSchPropsViewSet,
    SlctMonthlySalesPlanByIdViewSet,
    SlctMonthlySalesPlanDownloadViewSet,
    SlctMonthlySalesPlanViewSet,
    SlctNewMarketPricingRequestByIdViewSet,
    SlctNewMarketPricingRequestViewSet,
    SlctPartyWiseSchemePropsByIdViewSet,
    SlctPartyWiseSchemePropsViewSet,
    SlctPriceChangeRequestExistingMarktByIdViewSet,
    SlctPriceChangeRequestExistingMarktViewSet,
    SlctPrmPrdComboScmPropsByIdViewSet,
    SlctPrmPrdComboScmPropsViewSet,
    SlctQuantitySlabPropsByIdViewSet,
    SlctQuantitySlabPropsViewSet,
    SlctRailBasedSchPropsByIdViewSet,
    SlctRailBasedSchPropsViewSet,
    SlctSchemeDiscountProposalViewSet,
    SlctVehicleSchPropsByIdViewSet,
    SlctVehicleSchPropsViewSet,
    SlctVolCutterSlabBasedProposalByIdViewSet,
    SlctVolCutterSlabBasedProposalViewSet,
    SlctVolCutterTargetBasedByIdViewSet,
    SlctVolCutterTargetBasedViewSet,
    SponsorshipBudgetGetView,
    StateHeadMonthlySalesData,
    StateHeadMonthlySalesStateDropdown,
    StateHeadStateWiseTarget,
    TargetSalesPlanningMonthlyAdherenceViewswet,
    TargetSalesPlanningMonthlyTargetSum,
    TargetSalesPlanningMonthlyViewSet,
    TargetsalesPlanningSumCard,
    TgtPlantDepoMasterDropdown,
    TNmOmxSchemesViewSet,
    TOebsXxsclVehicleMasterViewSet,
    TradeOrderPlacementApprovalDropdown,
    UpdateSlctActivityPropsViewSet,
    UpdateSlctAnnualDiscSlabBasedViewSet,
    UpdateSlctAnnualDiscTargetBasedViewSet,
    UpdateSlctBenchmarkChangeRequestViewSet,
    UpdateSlctBoosterPerDayGrowthSchemeViewSet,
    UpdateSlctBoosterPerDayTargetSchemeViewSet,
    UpdateSlctBorderDiscPropsViewSet,
    UpdateSlctCashDiscPropseViewSet,
    UpdateSlctCombSlabGrowthPropsViewSet,
    UpdateSlctDealerLinkedSchPropsViewSet,
    UpdateSlctDealerOutsBasedPropsViewSet,
    UpdateSlctDirPltBilngDiscPropsViewSet,
    UpdateSlctEngCashSchPtPropsViewSet,
    UpdateSlctInKindBoosterSchemePropsViewSet,
    UpdateSlctInKindTourPropsalViewSet,
    UpdateSlctMasonKindSchPropsViewSet,
    UpdateSlctNewMarketPricingRequestViewSet,
    UpdateSlctPartyWiseSchemePropsViewSet,
    UpdateSlctPriceChangeRequestExistingMarktViewSet,
    UpdateSlctPrmPrdComboScmPropsViewSet,
    UpdateSlctQuantitySlabPropsViewSet,
    UpdateSlctRailBasedSchPropsViewSet,
    UpdateSlctSchemeDiscountProposalViewSet,
    UpdateSlctVehicleSchPropsViewSet,
    UpdateSlctVolCutterSlabBasedProposalViewSet,
    UpdateSlctVolCutterTargetBasedViewSet,
    ZoneMappingNewDropdown,
)
from .technical_head_views import (
    CrmAnnualSiteConvDropdown,
    CrmAnnualSiteConvPlanMonthlyViewSet,
    CrmAnnualSiteConvPlanViewSet,
    CrmMabRateListUploadDownloadAPIView,
    CrmMaterialtestCertificateViewSet,
    CrmNthActivityPlanByIdViewSet,
    CrmNthActivityPlanView,
    CrmNthProductApprovalDropdown,
    CrmNthProductApprovalViewSet,
    GetLstYrAvgCrmAnnualSiteConvPlanViewSet,
    GetPrvYrSelectdMnthCrmNthActivityPlanViewSet,
    GetPrvYrSelectdMnthNthBudgetPlanViewSet,
    NthBudgetPlanMonthlyViewSet,
    NthBudgetPlanViewSet,
    PreviousYearMonthAnnualSiteConvPlan,
)
