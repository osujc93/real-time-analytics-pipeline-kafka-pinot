from typing import Dict, Any, List

class ProductCatalog:

    _PRODUCTS: Dict[str, Dict[str, Any]] = {

        "DOG_DRY_PURINA_PRO_PLAN_HIGH_PROTEIN_CHICKEN_RICE_5LB": {
            "name": "Purina Pro Plan High Protein Shredded Blend Chicken & Rice Formula with Probiotics Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_HIGH_PROTEIN_CHICKEN_RICE_15LB": {
            "name": "Purina Pro Plan High Protein Shredded Blend Chicken & Rice Formula with Probiotics Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_HIGH_PROTEIN_CHICKEN_RICE_35LB": {
            "name": "Purina Pro Plan High Protein Shredded Blend Chicken & Rice Formula with Probiotics Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 75.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_HIGH_PROTEIN_CHICKEN_RICE_47LB": {
            "name": "Purina Pro Plan High Protein Shredded Blend Chicken & Rice Formula with Probiotics Dry Dog Food, 47-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 99.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_SALMON_RICE_4LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 22.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_SALMON_RICE_16LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 55.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_SALMON_RICE_30LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 79.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_SALMON_RICE_40LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 40-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 97.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_LAMB_OAT_4LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 22.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_LAMB_OAT_16LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 55.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_LAMB_OAT_24LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 69.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_LAMB_OAT_32LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 32-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 79.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_TURKEY_OAT_4LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 22.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_TURKEY_OAT_16LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 50.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_TURKEY_OAT_24LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 65.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SSS_TURKEY_OAT_32LB": {
            "name": "Purina Pro Plan Adult Sensitive Skin & Stomach Salmon & Rice Formula Dry Dog Food, 32-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 77.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_25.5LB": {
            "name": "Purina Pro Plan Adult Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 49.99
        },

        "DOG_DRY_PEDIGREE_7.7LB": {
            "name": "Pedigree Complete Nutrition - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_DRY_PEDIGREE_15.5LB": {
            "name": "Pedigree Complete Nutrition - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 26.99
        },
        "DOG_DRY_PEDIGREE_25.5LB": {
            "name": "Pedigree Complete Nutrition - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },

        "DOG_DRY_IAMS_7.7LB": {
            "name": "Iams Minichunks Adult Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_DRY_IAMS_15.5LB": {
            "name": "Iams Minichunks Adult Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_IAMS_25.5LB": {
            "name": "Iams Minichunks Adult Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },

        "DOG_DRY_EUKANUBA_7.7LB": {
            "name": "Eukanuba Adult Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 21.99
        },
        "DOG_DRY_EUKANUBA_15.5LB": {
            "name": "Eukanuba Adult Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 35.99
        },
        "DOG_DRY_EUKANUBA_25.5LB": {
            "name": "Eukanuba Adult Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 46.99
        },

        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_7.7LB": {
            "name": "Blue Buffalo Wilderness Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 25.99
        },
        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_15.5LB": {
            "name": "Blue Buffalo Wilderness Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 42.99
        },
        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_25.5LB": {
            "name": "Blue Buffalo Wilderness Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 54.99
        },

        "DOG_DRY_MERRICK_7.7LB": {
            "name": "Merrick Healthy Grains Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 24.99
        },
        "DOG_DRY_MERRICK_15.5LB": {
            "name": "Merrick Healthy Grains Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 40.99
        },
        "DOG_DRY_MERRICK_25.5LB": {
            "name": "Merrick Healthy Grains Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 52.99
        },

        "DOG_DRY_WELLNESS_7.7LB": {
            "name": "Wellness Complete Health Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 23.99
        },
        "DOG_DRY_WELLNESS_15.5LB": {
            "name": "Wellness Complete Health Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },
        "DOG_DRY_WELLNESS_25.5LB": {
            "name": "Wellness Complete Health Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 52.99
        },

        "DOG_DRY_HILLS_SCIENCE_DIET_7.7LB": {
            "name": "Hill’s Science Diet Adult Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 26.99
        },
        "DOG_DRY_HILLS_SCIENCE_DIET_15.5LB": {
            "name": "Hill’s Science Diet Adult Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },
        "DOG_DRY_HILLS_SCIENCE_DIET_25.5LB": {
            "name": "Hill’s Science Diet Adult Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 57.99
        },

        "DOG_DRY_BD_17_6LB": {
            "name": "Hill's Prescription Diet b/d Brain Aging Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_GD_17_6LB": {
            "name": "Hill's Prescription Diet g/d Aging Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_HD_17_6LB": {
            "name": "Hill's Prescription Diet h/d Heart Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_ID_8_5LB": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_ID_17_6LB": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_ID_STRESS_8_5LB": {
            "name": "Hill's Prescription Diet i/d Stress Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_ID_LOW_FAT_8_5LB": {
            "name": "Hill's Prescription Diet i/d Low Fat Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_ID_LOW_FAT_17_6LB": {
            "name": "Hill's Prescription Diet i/d Low Fat Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_CD_8_5LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_CD_17_6LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_CD_STRESS_8_5LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Stress Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_CD_STRESS_17_6LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Stress Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_CD_STRESS_METABOLIC_8_5LB": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_CD_STRESS_METABOLIC_17_6LB": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_DD_DUCK_8LB": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Duck & Potato (8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_DD_SALMON_8LB": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Salmon & Potato (8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_DD_VENISON_8LB": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Venison & Potato (8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_KD_CHICKEN_8_5LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_KD_CHICKEN_17_6LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_KD_LAMB_8_5LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Lamb Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_KD_LAMB_17_6LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Lamb Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_KD_EARLY_SUPPORT_17_6LB": {
            "name": "Hill's Prescription Diet k/d Early Support Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_JD_27_5LB": {
            "name": "Hill's Prescription Diet j/d Joint Care Chicken Flavor (27.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_KD_JD_18_7LB": {
            "name": "Hill's Prescription Diet k/d + j/d Kidney + Mobility Chicken Flavor (18.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_METABOLIC_8_5LB": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Flavor (8.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_METABOLIC_17_6LB": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_METABOLIC_27_5LB": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Flavor (27.5 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_METABOLIC_JD_24LB": {
            "name": "Hill's Prescription Diet Metabolic + Mobility Chicken Flavor (24 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_ZD_ORIGINAL_8LB": {
            "name": "Hill's Prescription Diet z/d Skin/Food Sensitivities Original Flavor (8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_ZD_ORIGINAL_17_6LB": {
            "name": "Hill's Prescription Diet z/d Skin/Food Sensitivities Original Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_ZD_LOW_FAT_8LB": {
            "name": "Hill's Prescription Diet z/d Low Fat Skin/Food Sensitivities Original Flavor (8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_ZD_LOW_FAT_17_6LB": {
            "name": "Hill's Prescription Diet z/d Low Fat Skin/Food Sensitivities Original Flavor (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_AD_CHICKEN_5_5OZ": {
            "name": "Hill's Prescription Diet a/d Urgent Care with Chicken (5.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_ID_CHICKEN_STEW_12_5OZ": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_ID_LOW_FAT_13OZ": {
            "name": "Hill's Prescription Diet i/d Low Fat Original Flavor (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_ID_STRESS_12_5OZ": {
            "name": "Hill's Prescription Diet i/d Stress Chicken & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_CD_STEW_12_5OZ": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_CD_STRESS_STEW_12_5OZ": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Stress Chicken & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_CD_STRESS_METABOLIC_12_5OZ": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_KD_CHICKEN_12_5OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care with Chicken (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_KD_LAMB_12_5OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care with Lamb (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_KD_BEEF_STEW_12_5OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care Beef & Vegetable Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_KD_JD_12_5OZ": {
            "name": "Hill's Prescription Diet k/d + j/d Kidney + Mobility Chicken Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_DD_DUCK_13OZ": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Duck Formula (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_DD_VENISON_13OZ": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Venison Formula (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_DD_SALMON_13OZ": {
            "name": "Hill's Prescription Diet d/d Skin/Food Sensitivities Salmon Formula (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_GD_CHICKEN_13OZ": {
            "name": "Hill's Prescription Diet g/d Aging Care Chicken Flavor (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_HD_CHICKEN_13OZ": {
            "name": "Hill's Prescription Diet h/d Heart Care Chicken Flavor (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_METABOLIC_STEW_12_5OZ": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_METABOLIC_JD_12_5OZ": {
            "name": "Hill's Prescription Diet Metabolic + Mobility Chicken Stew (12.5-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_ZD_13OZ": {
            "name": "Hill's Prescription Diet z/d Skin/Food Sensitivities Original Formula (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_ZD_LOW_FAT_13OZ": {
            "name": "Hill's Prescription Diet z/d Low Fat Skin/Food Sensitivities (13-oz can)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_KD_CHICKEN_4LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_KD_CHICKEN_8_5LB": {
            "name": "Hill's Prescription Diet k/d Kidney Care Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_KD_EARLY_4LB": {
            "name": "Hill's Prescription Diet k/d Early Support Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_KD_MOBILITY_4LB": {
            "name": "Hill's Prescription Diet k/d + Mobility Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_ID_CHICKEN_4LB": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_ID_CHICKEN_8_5LB": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_CD_CHICKEN_4LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_CD_CHICKEN_8_5LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_CD_STRESS_4LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Stress Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_CD_STRESS_8_5LB": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Stress Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_CD_STRESS_METABOLIC_4LB": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_CD_STRESS_METABOLIC_8_5LB": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_METABOLIC_4LB": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_METABOLIC_8_5LB": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_ZD_ORIGINAL_8LB": {
            "name": "Hill's Prescription Diet z/d Skin/Food Sensitivities Original Flavor (8 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_YD_THYROID_4LB": {
            "name": "Hill's Prescription Diet y/d Thyroid Care Chicken Flavor (4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_YD_THYROID_8_5LB": {
            "name": "Hill's Prescription Diet y/d Thyroid Care Chicken Flavor (8.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_AD_CHICKEN_5_5OZ": {
            "name": "Hill's Prescription Diet a/d Urgent Care with Chicken (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_ID_STEW_5_5OZ": {
            "name": "Hill's Prescription Diet i/d Digestive Care Chicken & Vegetable Stew (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_CD_5_5OZ": {
            "name": "Hill's Prescription Diet c/d Multicare Urinary Care Chicken (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_CD_STRESS_5_5OZ": {
            "name": "Hill's Prescription Diet c/d Urinary Stress Chicken (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_POUCH_CD_STRESS_METABOLIC_2_9OZ": {
            "name": "Hill's Prescription Diet c/d Urinary Stress + Metabolic Chicken (2.9-oz pouch)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_KD_CHICKEN_5_5OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care with Chicken (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_POUCH_KD_SALMON_2_9OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care Salmon & Vegetable Stew (2.9-oz pouch)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_POUCH_KD_BEEF_2_9OZ": {
            "name": "Hill's Prescription Diet k/d Kidney Care Beef & Vegetable Stew (2.9-oz pouch)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_POUCH_METABOLIC_2_9OZ": {
            "name": "Hill's Prescription Diet Metabolic Weight Management Chicken (2.9-oz pouch)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_YD_THYROID_5_5OZ": {
            "name": "Hill's Prescription Diet y/d Thyroid Care Chicken (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_ZD_5_5OZ": {
            "name": "Hill's Prescription Diet z/d Skin/Food Sensitivities Original Formula (5.5-oz can)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },

        "DOG_DRY_ROYAL_CANIN_7.7LB": {
            "name": "Royal Canin Canine Health Nutrition - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 27.99
        },
        "DOG_DRY_ROYAL_CANIN_15.5LB": {
            "name": "Royal Canin Canine Health Nutrition - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 49.99
        },
        "DOG_DRY_ROYAL_CANIN_25.5LB": {
            "name": "Royal Canin Canine Health Nutrition - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 64.99
        },

        "DOG_DRY_URINARY_SO_6_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Dry Dog Food (6.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_URINARY_SO_17_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_URINARY_SO_25_3LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Dry Dog Food (25.3 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_URINARY_SO_MODCAL_7_7LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Moderate Calorie Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_URINARY_SO_MODCAL_17_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Moderate Calorie Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_URINARY_SO_HP_7_7LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO + Hydrolyzed Protein Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_URINARY_SO_HP_17_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO + Hydrolyzed Protein Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_HYDRO_HP_8_8LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein HP Dry Dog Food (8.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_HYDRO_HP_19_8LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein HP Dry Dog Food (19.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_HYDRO_HP_MODCAL_8_8LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein Moderate Calorie Dry Dog Food (8.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_HYDRO_HP_MODCAL_19_8LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein Moderate Calorie Dry Dog Food (19.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_RENAL_A_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support A Dry Dog Food (6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_RENAL_A_17_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support A Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_RENAL_F_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support F Dry Dog Food (6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_RENAL_F_17_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support F Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_RENAL_S_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support S Dry Dog Food (6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_RENAL_S_17_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support S Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_GLYCOBALANCE_6_6LB": {
            "name": "Royal Canin Veterinary Diet Glycobalance Dry Dog Food (6.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_GLYCOBALANCE_22LB": {
            "name": "Royal Canin Veterinary Diet Glycobalance Dry Dog Food (22 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_GI_6_6LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Dry Dog Food (6.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_GI_22LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Dry Dog Food (22 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_GI_LOW_FAT_6_6LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Low Fat Dry Dog Food (6.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_GI_LOW_FAT_17_6LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Low Fat Dry Dog Food (17.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_GI_HIGH_ENERGY_8_8LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal High Energy Dry Dog Food (8.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_GI_FIBER_RESPONSE_8_8LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Fiber Response Dry Dog Food (8.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_SELECTED_PROT_PD_7_7LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PD (Potato & Duck) Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_SELECTED_PROT_PR_7_7LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PR (Potato & Rabbit) Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_SELECTED_PROT_PV_7_7LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PV (Potato & Venison) Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_SELECTED_PROT_PW_7_7LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PW (Potato & Whitefish) Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_ULTAMINO_8_8LB": {
            "name": "Royal Canin Veterinary Diet Ultamino Dry Dog Food (8.8 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_SATIETY_SUPPORT_7_7LB": {
            "name": "Royal Canin Veterinary Diet Satiety Support Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_CALM_4_4LB": {
            "name": "Royal Canin Veterinary Diet Calm Small Dog Dry Dog Food (4.4 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_DENTAL_7_7LB": {
            "name": "Royal Canin Veterinary Diet Dental Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_EARLY_CARDIAC_7_7LB": {
            "name": "Royal Canin Veterinary Diet Early Cardiac Dry Dog Food (7.7 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_SKIN_SUPPORT_6_6LB": {
            "name": "Royal Canin Veterinary Diet Skin Support Dry Dog Food (6.6 lb)",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_URINARY_SO_LOAF_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Urinary SO Loaf Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_GI_LOW_FAT_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Low Fat Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_GI_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_RENAL_A_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Renal Support A Loaf Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_HYDRO_HP_13_7OZ": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein HP Canned Dog Food (13.7 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_GLYCOBALANCE_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Glycobalance Thin Slices in Gravy Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_CAN_ULTAMINO_13_7OZ": {
            "name": "Royal Canin Veterinary Diet Ultamino Canned Dog Food (13.7 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_CAN_SATIETY_SUPPORT_13_5OZ": {
            "name": "Royal Canin Veterinary Diet Satiety Support Loaf Canned Dog Food (13.5 oz)",
            "category": "Wet Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_URINARY_SO_7_7LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Dry Cat Food (7.7 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_URINARY_SO_17_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Dry Cat Food (17.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_URINARY_SO_MODCAL_6_6LB": {
            "name": "Royal Canin Veterinary Diet Urinary SO Moderate Calorie Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_URINARY_CALM_6_6LB": {
            "name": "Royal Canin Veterinary Diet Multifunction Urinary + Calm Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_URINARY_HP_6_6LB": {
            "name": "Royal Canin Veterinary Diet Multifunction Urinary + Hydrolyzed Protein Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_HYDRO_HP_7_7LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein HP Dry Cat Food (7.7 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_HYDRO_HP_MODCAL_6_6LB": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein Moderate Calorie Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_RENAL_A_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support A Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_RENAL_D_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support D Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_RENAL_E_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support E Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_RENAL_F_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support F Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_RENAL_S_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support S Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_RENAL_T_6_6LB": {
            "name": "Royal Canin Veterinary Diet Renal Support T Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_GLYCOBALANCE_4_4LB": {
            "name": "Royal Canin Veterinary Diet Glycobalance Dry Cat Food (4.4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_HEPATIC_4_4LB": {
            "name": "Royal Canin Veterinary Diet Hepatic Dry Cat Food (4.4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_GI_7_7LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Dry Cat Food (7.7 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_GI_FIBER_RESPONSE_8_8LB": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Fiber Response Dry Cat Food (8.8 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_SELECTED_PROT_PD_6_6LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PD (Pea & Duck) Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_SELECTED_PROT_PR_6_6LB": {
            "name": "Royal Canin Veterinary Diet Selected Protein PR (Pea & Rabbit) Dry Cat Food (6.6 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_ULTAMINO_5_5LB": {
            "name": "Royal Canin Veterinary Diet Ultamino Dry Cat Food (5.5 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_SATIETY_SUPPORT_7_7LB": {
            "name": "Royal Canin Veterinary Diet Satiety Support Dry Cat Food (7.7 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_CALM_4_4LB": {
            "name": "Royal Canin Veterinary Diet Calm Dry Cat Food (4.4 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_DRY_DENTAL_6_2LB": {
            "name": "Royal Canin Veterinary Diet Dental Dry Cat Food (6.2 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_SKIN_SUPPORT_7_7LB": {
            "name": "Royal Canin Veterinary Diet Skin Support Dry Cat Food (7.7 lb)",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_URINARY_SO_GRAVY_5_1OZ": {
            "name": "Royal Canin Veterinary Diet Urinary SO Thin Slices in Gravy Canned Cat Food (5.1 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_GI_SLICES_3OZ": {
            "name": "Royal Canin Veterinary Diet Gastrointestinal Thin Slices in Gravy Canned Cat Food (3 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_RENAL_A_3OZ": {
            "name": "Royal Canin Veterinary Diet Renal Support A Morsels in Gravy Canned Cat Food (3 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_RENAL_T_3OZ": {
            "name": "Royal Canin Veterinary Diet Renal Support T Morsels in Gravy Canned Cat Food (3 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_HYDRO_HP_LOAF_5_1OZ": {
            "name": "Royal Canin Veterinary Diet Hydrolyzed Protein Loaf Canned Cat Food (5.1 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_GLYCOBALANCE_3OZ": {
            "name": "Royal Canin Veterinary Diet Glycobalance Thin Slices in Gravy Canned Cat Food (3 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_ULTAMINO_LOAF_5_1OZ": {
            "name": "Royal Canin Veterinary Diet Ultamino Loaf Canned Cat Food (5.1 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_SATIETY_SUPPORT_3OZ": {
            "name": "Royal Canin Veterinary Diet Satiety Support Loaf Canned Cat Food (3 oz)",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },

        "DOG_DRY_NUTRO_7.7LB": {
            "name": "Nutro Wholesome Essentials Dry Dog Food - 7.7 lbs",
            "category": "Dry Dry Dog Food (Non-Prescription)",
            "price": 22.99
        },
        "DOG_DRY_NUTRO_15.5LB": {
            "name": "Nutro Wholesome Essentials Dry Dog Food - 15.5 lbs",
            "category": "Dry Dry Dog Food (Non-Prescription)",
            "price": 37.99
        },
        "DOG_DRY_NUTRO_25.5LB": {
            "name": "Nutro Wholesome Essentials Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 48.99
        },

        "DOG_DRY_TASTE_OF_THE_WILD_7.7LB": {
            "name": "Taste of the Wild Roasted Bison & Venison - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 23.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_15.5LB": {
            "name": "Taste of the Wild Roasted Bison & Venison - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_25.5LB": {
            "name": "Taste of the Wild Roasted Bison & Venison - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 52.99
        },

        "DOG_DRY_RACHAEL_RAY_7.7LB": {
            "name": "Rachael Ray Nutrish Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_DRY_RACHAEL_RAY_15.5LB": {
            "name": "Rachael Ray Nutrish Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 31.99
        },
        "DOG_DRY_RACHAEL_RAY_25.5LB": {
            "name": "Rachael Ray Nutrish Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 42.99
        },

        "DOG_DRY_INSTINCT_7.7LB": {
            "name": "Instinct Original Grain-Free Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 28.99
        },
        "DOG_DRY_INSTINCT_15.5LB": {
            "name": "Instinct Original Grain-Free Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 49.99
        },
        "DOG_DRY_INSTINCT_25.5LB": {
            "name": "Instinct Original Grain-Free Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 64.99
        },

        "DOG_DRY_ORIJEN_7.7LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_DRY_ORIJEN_15.5LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "DOG_DRY_ORIJEN_25.5LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 79.99
        },

        "DOG_DRY_ACANA_7.7LB": {
            "name": "Acana Regionals Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_ACANA_15.5LB": {
            "name": "Acana Regionals Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 54.99
        },
        "DOG_DRY_ACANA_25.5LB": {
            "name": "Acana Regionals Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 74.99
        },

        "DOG_DRY_VICTOR_7.7LB": {
            "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_DRY_VICTOR_15.5LB": {
            "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_DRY_VICTOR_25.5LB": {
            "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 46.99
        },

        "DOG_DRY_HONEST_KITCHEN_7.7LB": {
            "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_DRY_HONEST_KITCHEN_15.5LB": {
            "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 57.99
        },
        "DOG_DRY_HONEST_KITCHEN_25.5LB": {
            "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 79.99
        },

        "DOG_DRY_EARTHBORN_7.7LB": {
            "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 24.99
        },
        "DOG_DRY_EARTHBORN_15.5LB": {
            "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 41.99
        },
        "DOG_DRY_EARTHBORN_25.5LB": {
            "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 54.99
        },

        "DOG_DRY_NATURES_RECIPE_7.7LB": {
            "name": "Nature’s Recipe Adult Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 17.99
        },
        "DOG_DRY_NATURES_RECIPE_15.5LB": {
            "name": "Nature’s Recipe Adult Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 28.99
        },
        "DOG_DRY_NATURES_RECIPE_25.5LB": {
            "name": "Nature’s Recipe Adult Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 42.99
        },

        "DOG_DRY_SOLID_GOLD_7.7LB": {
            "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 22.99
        },
        "DOG_DRY_SOLID_GOLD_15.5LB": {
            "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 36.99
        },
        "DOG_DRY_SOLID_GOLD_25.5LB": {
            "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 49.99
        },

        "DOG_DRY_CANIDAE_7.7LB": {
            "name": "Canidae All Life Stages Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 24.99
        },
        "DOG_DRY_CANIDAE_15.5LB": {
            "name": "Canidae All Life Stages Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },
        "DOG_DRY_CANIDAE_25.5LB": {
            "name": "Canidae All Life Stages Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 54.99
        },

        "DOG_DRY_NATURAL_BALANCE_7.7LB": {
            "name": "Natural Balance L.I.D. Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 25.99
        },
        "DOG_DRY_NATURAL_BALANCE_15.5LB": {
            "name": "Natural Balance L.I.D. Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },
        "DOG_DRY_NATURAL_BALANCE_25.5LB": {
            "name": "Natural Balance L.I.D. Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },

        "DOG_DRY_WHOLE_EARTH_FARMS_7.7LB": {
            "name": "Whole Earth Farms Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 16.99
        },
        "DOG_DRY_WHOLE_EARTH_FARMS_15.5LB": {
            "name": "Whole Earth Farms Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_WHOLE_EARTH_FARMS_25.5LB": {
            "name": "Whole Earth Farms Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },

        "DOG_DRY_AMERICAN_JOURNEY_7.7LB": {
            "name": "American Journey Active Life Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_DRY_AMERICAN_JOURNEY_15.5LB": {
            "name": "American Journey Active Life Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 32.99
        },
        "DOG_DRY_AMERICAN_JOURNEY_25.5LB": {
            "name": "American Journey Active Life Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },

        "DOG_DRY_CESAR_7.7LB": {
            "name": "Cesar Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 21.99
        },
        "DOG_DRY_CESAR_15.5LB": {
            "name": "Cesar Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 35.99
        },
        "DOG_DRY_CESAR_25.5LB": {
            "name": "Cesar Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 46.99
        },

        "DOG_DRY_FROMM_7.7LB": {
            "name": "Fromm Adult Gold Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_FROMM_15.5LB": {
            "name": "Fromm Adult Gold Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 49.99
        },
        "DOG_DRY_FROMM_25.5LB": {
            "name": "Fromm Adult Gold Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 64.99
        },

        "DOG_DRY_TIKI_DOG_7.7LB": {
            "name": "Tiki Dog Aloha Pet Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 28.99
        },
        "DOG_DRY_TIKI_DOG_15.5LB": {
            "name": "Tiki Dog Aloha Pet Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },
        "DOG_DRY_TIKI_DOG_25.5LB": {
            "name": "Tiki Dog Aloha Pet Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },

        "DOG_DRY_FARMINA_7.7LB": {
            "name": "Farmina N&D Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_DRY_FARMINA_15.5LB": {
            "name": "Farmina N&D Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "DOG_DRY_FARMINA_25.5LB": {
            "name": "Farmina N&D Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 79.99
        },

        "DOG_DRY_BIL_JAC_7.7LB": {
            "name": "Bil-Jac Adult Select Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_DRY_BIL_JAC_15.5LB": {
            "name": "Bil-Jac Adult Select Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_BIL_JAC_25.5LB": {
            "name": "Bil-Jac Adult Select Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },

        "DOG_DRY_ZIGNATURE_7.7LB": {
            "name": "Zignature Grain-Free Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 24.99
        },
        "DOG_DRY_ZIGNATURE_15.5LB": {
            "name": "Zignature Grain-Free Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },
        "DOG_DRY_ZIGNATURE_25.5LB": {
            "name": "Zignature Grain-Free Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 54.99
        },

        "DOG_DRY_DAVES_7.7LB": {
            "name": "Dave’s Pet Food Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 20.99
        },
        "DOG_DRY_DAVES_15.5LB": {
            "name": "Dave’s Pet Food Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_DRY_DAVES_25.5LB": {
            "name": "Dave’s Pet Food Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 48.99
        },

        "DOG_DRY_EAGLE_PACK_7.7LB": {
            "name": "Eagle Pack Original Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_DRY_EAGLE_PACK_15.5LB": {
            "name": "Eagle Pack Original Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 31.99
        },
        "DOG_DRY_EAGLE_PACK_25.5LB": {
            "name": "Eagle Pack Original Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 44.99
        },

        "DOG_DRY_DR_GARYS_BEST_BREED_7.7LB": {
            "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 7.7 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 25.99
        },
        "DOG_DRY_DR_GARYS_BEST_BREED_15.5LB": {
            "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 15.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 39.99
        },
        "DOG_DRY_DR_GARYS_BEST_BREED_25.5LB": {
            "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 25.5 lbs",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 56.99
        },

        "DOG_CANS_PURINA_PRO_PLAN_CASE12": {
            "name": "Purina Pro Plan Wet Dog Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_CANS_PURINA_PRO_PLAN_CASE24": {
            "name": "Purina Pro Plan Wet Dog Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 35.99
        },

        "DOG_CANS_PEDIGREE_CASE12": {
            "name": "Pedigree Chopped Wet Dog Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 17.99
        },
        "DOG_CANS_PEDIGREE_CASE24": {
            "name": "Pedigree Chopped Wet Dog Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 33.99
        },

        "DOG_CANS_IAMS_CASE12": {
            "name": "Iams ProActive Health Wet Dog Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_CANS_IAMS_CASE24": {
            "name": "Iams ProActive Health Wet Dog Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 34.99
        },

        "DOG_CANS_BLUE_BUFFALO_CASE12": {
            "name": "Blue Buffalo Homestyle Recipe Wet Dog Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 25.99
        },
        "DOG_CANS_BLUE_BUFFALO_CASE24": {
            "name": "Blue Buffalo Homestyle Recipe Wet Dog Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 47.99
        },

        "DOG_CANS_CESAR_CASE12": {
            "name": "Cesar Classic Loaf in Sauce Wet Dog Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_CANS_CESAR_CASE24": {
            "name": "Cesar Classic Loaf in Sauce Wet Dog Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 35.99
        },

        "CAT_DRY_PURINA_PRO_PLAN_4.4LB": {
            "name": "Purina Pro Plan Complete Dry Cat Food - 4.4 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 14.99
        },
        "CAT_DRY_PURINA_PRO_PLAN_12.2LB": {
            "name": "Purina Pro Plan Complete Dry Cat Food - 12.2 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 24.99
        },
        "CAT_DRY_PURINA_PRO_PLAN_19.8LB": {
            "name": "Purina Pro Plan Complete Dry Cat Food - 19.8 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 36.99
        },

        "CAT_DRY_MEOW_MIX_4.4LB": {
            "name": "Meow Mix Original Dry Cat Food - 4.4 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 9.99
        },
        "CAT_DRY_MEOW_MIX_12.2LB": {
            "name": "Meow Mix Original Dry Cat Food - 12.2 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 15.99
        },
        "CAT_DRY_MEOW_MIX_19.8LB": {
            "name": "Meow Mix Original Dry Cat Food - 19.8 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 23.99
        },

        "CAT_DRY_SHEBA_4.4LB": {
            "name": "Sheba Dry Cat Food - 4.4 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 12.99
        },
        "CAT_DRY_SHEBA_12.2LB": {
            "name": "Sheba Dry Cat Food - 12.2 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 21.99
        },
        "CAT_DRY_SHEBA_19.8LB": {
            "name": "Sheba Dry Cat Food - 19.8 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 29.99
        },

        "CAT_DRY_BLUE_BUFFALO_TASTEFULS_4.4LB": {
            "name": "Blue Buffalo Tastefuls Dry Cat Food - 4.4 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 16.99
        },
        "CAT_DRY_BLUE_BUFFALO_TASTEFULS_12.2LB": {
            "name": "Blue Buffalo Tastefuls Dry Cat Food - 12.2 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 27.99
        },
        "CAT_DRY_BLUE_BUFFALO_TASTEFULS_19.8LB": {
            "name": "Blue Buffalo Tastefuls Dry Cat Food - 19.8 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 42.99
        },

        "CAT_CANS_FANCY_FEAST_CASE24": {
            "name": "Fancy Feast Classic Wet Cat Food 5.5 oz (Case of 24)",
            "category": "Cat Food (Non-Prescription)",
            "price": 18.99
        },
        "CAT_CANS_FANCY_FEAST_CASE12": {
            "name": "Fancy Feast Classic Wet Cat Food 5.5 oz (Case of 12)",
            "category": "Cat Food (Non-Prescription)",
            "price": 9.99
        },

        "CAT_CAN_FRISKIES_PATE_MIXED_GRILL_CASE24": {
            "name": "Friskies Classic Pate Mixed Grill, 5.5-oz cans (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_TURKEY_GIBLETS_CASE24": {
            "name": "Friskies Classic Pate Turkey & Giblets Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_SALMON_CASE24": {
            "name": "Friskies Classic Pate Salmon Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_OCEAN_WHITEFISH_TUNA_CASE24": {
            "name": "Friskies Classic Pate Ocean Whitefish & Tuna Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_LIVER_CHICKEN_CASE24": {
            "name": "Friskies Classic Pate Liver & Chicken Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_COUNTRY_STYLE_CASE24": {
            "name": "Friskies Pate Country Style Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 24.56
        },
        "CAT_CAN_FRISKIES_PATE_POULTRY_PLATTER_CASE24": {
            "name": "Friskies Classic Pate Poultry Platter, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_CHICKEN_TUNA_CASE24": {
            "name": "Friskies Classic Pate Chicken & Tuna Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },
        "CAT_CAN_FRISKIES_PATE_INDOOR_CHICKEN_CASE24": {
            "name": "Friskies Indoor Classic Pate Chicken Dinner, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },

        "CAT_CAN_FRISKIES_FILETS_CHICKEN_GRAVY_CASE24": {
            "name": "Friskies Prime Filets Chicken in Gravy, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },

        "CAT_CAN_FRISKIES_SHREDS_CHICKEN_GRAVY_CASE24": {
            "name": "Friskies Savory Shreds with Chicken in Gravy, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },

        "CAT_CAN_FRISKIES_EXTRA_GRAVY_CHUNKY_CHICKEN_CASE24": {
            "name": "Friskies Extra Gravy Chunky Chicken in Savory Gravy, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.72
        },

        "CAT_CAN_FRISKIES_VAR_CLASSIC_PATE_CASE24": {
            "name": "Friskies Classic Pate Favorites Variety Pack, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 18.69
        },
        "CAT_CAN_FRISKIES_VAR_SURFIN_TURFIN_CASE40": {
            "name": "Friskies Surfin' & Turfin' Favorites Variety Pack, 5.5-oz (Case 40)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 31.68
        },
        "CAT_CAN_FRISKIES_VAR_SHREDS_CASE40": {
            "name": "Friskies Shreds in Gravy Variety Pack, 5.5-oz (Case 40)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 30.46
        },
        "CAT_CAN_FRISKIES_VAR_EXTRA_GRAVY_CHUNKY_CASE24": {
            "name": "Friskies Extra Gravy Chunky Variety Pack, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 21.12
        },
        "CAT_CAN_FRISKIES_VAR_FARM_FAVORITES_CASE24": {
            "name": "Friskies Farm Favorites Chicken & Carrots / Salmon & Spinach Pate Variety Pack, 5.5-oz (Case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 20.64
        },

        "CAT_CAN_FRISKIES_PATE_MIXED_GRILL_CASE12": {
            "name": "Friskies Classic Pate Mixed Grill, 5.5-oz cans (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_TURKEY_GIBLETS_CASE12": {
            "name": "Friskies Classic Pate Turkey & Giblets Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_SALMON_CASE12": {
            "name": "Friskies Classic Pate Salmon Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_OCEAN_WHITEFISH_TUNA_CASE12": {
            "name": "Friskies Classic Pate Ocean Whitefish & Tuna Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_LIVER_CHICKEN_CASE12": {
            "name": "Friskies Classic Pate Liver & Chicken Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_COUNTRY_STYLE_CASE12": {
            "name": "Friskies Pate Country Style Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_POULTRY_PLATTER_CASE12": {
            "name": "Friskies Classic Pate Poultry Platter, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_CHICKEN_TUNA_CASE12": {
            "name": "Friskies Classic Pate Chicken & Tuna Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },
        "CAT_CAN_FRISKIES_PATE_INDOOR_CHICKEN_CASE12": {
            "name": "Friskies Indoor Classic Pate Chicken Dinner, 5.5-oz (Case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 9.36
        },

        "CAT_CANS_SHEBA_CASE24": {
            "name": "Sheba Perfect Portions 5.5 oz (Case of 24)",
            "category": "Cat Food (Non-Prescription)",
            "price": 21.99
        },
        "CAT_CANS_SHEBA_CASE12": {
            "name": "Sheba Perfect Portions 5.5 oz (Case of 12)",
            "category": "Cat Food (Non-Prescription)",
            "price": 11.99
        },

        "CAT_CANS_BLUE_BUFFALO_CASE24": {
            "name": "Blue Buffalo Wilderness Wet Cat Food 5.5 oz (Case of 24)",
            "category": "Cat Food (Non-Prescription)",
            "price": 29.99
        },
        "CAT_CANS_BLUE_BUFFALO_CASE12": {
            "name": "Blue Buffalo Wilderness Wet Cat Food 5.5 oz (Case of 12)",
            "category": "Cat Food (Non-Prescription)",
            "price": 15.99
        },

        "DOG_TREAT_MILK_BONE_40OZ": {
            "name": "Milk-Bone MaroSnacks Real Bone Marrow Dog Treats, 40-oz tub",
            "category": "Dog Treats (Non-Prescription)",
            "price": 6.99
        },
        "DOG_TREAT_PUP_PERONI_225OZ": {
            "name": "Pup-Peroni Original Beef Flavor Dog Treats, 22.5-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 4.99
        },
        "DOG_TREAT_BLUE_BUFFALO_12OZ": {
            "name": "Blue Buffalo True Chews Chicken Pot Pie Recipe Dog Treats, 12-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.99
        },
        "DOG_TREAT_GREENIES_CHICKEN_43CNT": {
            "name": "Greenies Teenie Original Chicken Flavor Dental Dog Treats, 43 count",
            "category": "Dog Treats (Non-Prescription)",
            "price": 15.99
        },
        "DOG_TREAT_FULL_MOON_JERKY_24OZ": {
            "name": "Full Moon Chicken Jerky Human-Grade Dog Treats, 24-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 11.49
        },
        "DOG_TREAT_K9_CARRY_BCN_CHEESE_45OZ": {
            "name": "Canine Carry Outs Bacon & Cheese Flavor Dog Treats, 4.5-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 9.49
        },
        "DOG_TREAT_BB_HEALTH_BCN_EGG_CHS_16OZ": {
            "name": "Blue Buffalo Health Bars Baked with Bacon, Egg & Cheese Dog Treats, 16-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 9.99
        },
        "DOG_TREAT_DREAMBONE_CHICKEN_VP_18CNT": {
            "name": "DreamBone Spirals Variety Pack Real Chicken, Beef, Bacon, Cheese, Sweet Potato & Wholesome Vegetables Rawhide-Free Dog Chews, 18 count",
            "category": "Dog Treats (Non-Prescription)",
            "price": 12.99
        },
        "DOG_TREAT_PURINA_BENEFUL_DLGHT_APP_PEAS_PNT_BTTR_36OZ": {
            "name": "Purina Beneful Baked Delights Snackers with Apples, Carrots, Peas & Peanut Butter Dog Treats, 36-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 7.99
        },
        "DOG_TREAT_OLD_MOTHER_HUBBARD": {
            "name": "Old Mother Hubbard Crunchy Dog Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 5.99
        },
        "DOG_TREAT_BOCCES_BAKERY": {
            "name": "Bocce’s Bakery Dog Biscuits",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.49
        },
        "DOG_TREAT_THREE_DOG_BAKERY": {
            "name": "Three Dog Bakery Dog Cookies",
            "category": "Dog Treats (Non-Prescription)",
            "price": 7.99
        },
        "DOG_TREAT_BIL_JAC": {
            "name": "Bil-Jac Soft Training Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 6.99
        },
        "DOG_TREAT_NATURAL_BALANCE": {
            "name": "Natural Balance Limited Ingredient Dog Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.99
        },
        "DOG_TREAT_WHIMZEES": {
            "name": "Whimzees Dental Chews",
            "category": "Dog Treats (Non-Prescription)",
            "price": 14.99
        },
        "DOG_TREAT_TRUE_CHEWS": {
            "name": "True Chews Premium Jerky",
            "category": "Dog Treats (Non-Prescription)",
            "price": 12.99
        },
        "DOG_TREAT_PLATO": {
            "name": "Plato Pet Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 10.99
        },
        "DOG_TREAT_NATURE_GNAWS": {
            "name": "Nature Gnaws Bully Sticks",
            "category": "Dog Treats (Non-Prescription)",
            "price": 16.99
        },
        "DOG_TREAT_ETTA_SAYS": {
            "name": "Etta Says! Crunchy Deer Chews",
            "category": "Dog Treats (Non-Prescription)",
            "price": 11.99
        },
        "DOG_TREAT_CADET": {
            "name": "Cadet Chicken & Duck Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 9.99
        },
        "DOG_TREAT_REDBARN": {
            "name": "Redbarn Natural Dog Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.49
        },
        "DOG_TREAT_BULLYMAKE": {
            "name": "Bullymake Tough Chew Treats",
            "category": "Dog Treats (Non-Prescription)",
            "price": 13.99
        },
        "DOG_TREAT_CANINE_NATURALS": {
            "name": "Canine Naturals Hide Free Chews",
            "category": "Dog Treats (Non-Prescription)",
            "price": 7.99
        },
        "DOG_TREAT_3_DOG_BKRY_VANILLA_26OZ": {
            "name": "Three Dog Bakery Soft Baked AssortMutt Trio, Oat, PB, & Vanilla Dog Treats, 26-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.99
        },
        "DOG_TREAT_SIMPLE_FOOD_CHKN_TREATS_27OZ": {
            "name": "Simple Food Project Chicken Heart Freeze-Dried Dog Treats, 2.7-oz",
            "category": "Dog Treats (Non-Prescription)",
            "price": 12.99
        },
        "DOG_TREAT_NEWMAN_BCN_BRRY_SOFT_10OZ": {
            "name": "Newman's Own Bacon & Berries Recipe Woofles Soft & Chewy Dog Treats, 10-oz bag",
            "category": "Dog Treats (Non-Prescription)",
            "price": 9.49
        },

        "CAT_TREAT_TEMPTATIONS": {
            "name": "Temptations Classic Crunchy Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 5.99
        },
        "CAT_TREAT_FELINE_GREENIES": {
            "name": "Feline Greenies Dental Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 6.49
        },
        "CAT_TREAT_BLUE_BUFFALO_BURSTS": {
            "name": "Blue Buffalo Wilderness Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 7.99
        },
        "CAT_TREAT_FRISKIES_PARTY_MIX": {
            "name": "Friskies Party Mix Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 4.99
        },
        "CAT_TREAT_SHEBA_MEATY_STICKS": {
            "name": "Sheba Meaty Sticks",
            "category": "Cat Treats (Non-Prescription)",
            "price": 5.49
        },
        "CAT_TREAT_MEOW_MIX_BRUSHING_BITES": {
            "name": "Meow Mix Brushing Bites Dental Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 3.99
        },
        "CAT_TREAT_WELLNESS_KITTLES": {
            "name": "Wellness Kittles Crunchy Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 5.49
        },
        "CAT_TREAT_HARTZ_DELECTABLES": {
            "name": "Hartz Delectables Squeeze Ups",
            "category": "Cat Treats (Non-Prescription)",
            "price": 6.99
        },
        "CAT_TREAT_TIKI_CAT_STIX": {
            "name": "Tiki Cat Stix Wet Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 8.49
        },
        "CAT_TREAT_INSTINCT_FREEZE_DRIED": {
            "name": "Instinct Raw Boost Mixers",
            "category": "Cat Treats (Non-Prescription)",
            "price": 9.99
        },
        "CAT_TREAT_STELLA_CHEWYS_FREEZE_DRIED": {
            "name": "Stella & Chewy’s Freeze-Dried Cat Morsels",
            "category": "Cat Treats (Non-Prescription)",
            "price": 11.99
        },
        "CAT_TREAT_NULO": {
            "name": "Nulo Freestyle Grain-Free Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 7.99
        },
        "CAT_TREAT_VITAL_ESSENTIALS": {
            "name": "Vital Essentials Freeze-Dried Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 12.99
        },
        "CAT_TREAT_PUREBITES": {
            "name": "PureBites Freeze-Dried Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 5.99
        },
        "CAT_TREAT_WHOLE_LIFE": {
            "name": "Whole Life Freeze-Dried Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 8.99
        },
        "CAT_TREAT_FANCY_FEAST": {
            "name": "Fancy Feast Cat Treats (Purina)",
            "category": "Cat Treats (Non-Prescription)",
            "price": 4.99
        },
        "CAT_TREAT_RACHAEL_RAY_NUTRISH": {
            "name": "Rachael Ray Nutrish LoveBites Cat Treats",
            "category": "Cat Treats (Non-Prescription)",
            "price": 6.49
        },

        "DOG_RAW_SC_CHICKEN_PATTIES_14OZ": {
            "name": "Stella & Chewy's Chicken Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_SC_CHICKEN_PATTIES_25OZ": {
            "name": "Stella & Chewy's Chicken Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_SC_SUPER_BEEF_PATTIES_14OZ": {
            "name": "Stella & Chewy's Super Beef Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_SC_SUPER_BEEF_PATTIES_25OZ": {
            "name": "Stella & Chewy's Super Beef Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_SC_DUCK_DUCK_GOOSE_PATTIES_14OZ": {
            "name": "Stella & Chewy's Duck Duck Goose Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_SC_DUCK_DUCK_GOOSE_PATTIES_25OZ": {
            "name": "Stella & Chewy's Duck Duck Goose Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_SC_SURF_TURF_PATTIES_14OZ": {
            "name": "Stella & Chewy's Surf Turf Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_SC_SURF_TURF_PATTIES_25OZ": {
            "name": "Stella & Chewy's Surf Turf Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_SC_LAMB_PATTIES_14OZ": {
            "name": "Stella & Chewy's Lamb Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_SC_LAMB_PATTIES_25OZ": {
            "name": "Stella & Chewy's Lamb Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_SC_VENISON_PATTIES_14OZ": {
            "name": "Stella & Chewy's Venison Dinner Patties Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_SC_VENISON_PATTIES_25OZ": {
            "name": "Stella & Chewy's Venison Dinner Patties Freeze-Dried Raw Dog Food, 25-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_TOPPER_SC_MEALMIXERS_CHICKEN_18OZ": {
            "name": "Stella & Chewy's Meal Mixers Chicken Freeze-Dried Raw Dog Food Topper, 18-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_TOPPER_SC_MEALMIXERS_BEEF_18OZ": {
            "name": "Stella & Chewy's Meal Mixers Beef Freeze-Dried Raw Dog Food Topper, 18-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_TOPPER_SC_MEALMIXERS_TURKEY_18OZ": {
            "name": "Stella & Chewy's Meal Mixers Turkey Freeze-Dried Raw Dog Food Topper, 18-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_TOPPER_SC_MEALMIXERS_DUCK_18OZ": {
            "name": "Stella & Chewy's Meal Mixers Duck Freeze-Dried Raw Dog Food Topper, 18-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_PRIMAL_BEEF_NUGGETS_14OZ": {
            "name": "Primal Beef Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_PRIMAL_CHICKEN_SALMON_NUGGETS_14OZ": {
            "name": "Primal Chicken & Salmon Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_PRIMAL_TURKEY_SARDINE_NUGGETS_14OZ": {
            "name": "Primal Turkey & Sardine Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_PRIMAL_LAMB_NUGGETS_14OZ": {
            "name": "Primal Lamb Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_PRIMAL_DUCK_NUGGETS_14OZ": {
            "name": "Primal Duck Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_PRIMAL_VENISON_NUGGETS_14OZ": {
            "name": "Primal Venison Formula Nuggets Grain-Free Freeze-Dried Raw Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_TOPPER_INSTINCT_CHICKEN_14OZ": {
            "name": "Instinct Raw Boost Mixers Chicken Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_TOPPER_INSTINCT_BEEF_14OZ": {
            "name": "Instinct Raw Boost Mixers Beef Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_TOPPER_INSTINCT_LAMB_14OZ": {
            "name": "Instinct Raw Boost Mixers Lamb Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_TOPPER_INSTINCT_TURKEY_14OZ": {
            "name": "Instinct Raw Boost Mixers Turkey Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_TOPPER_INSTINCT_PUPPY_CHICKEN_14OZ": {
            "name": "Instinct Raw Boost Mixers Puppy Chicken Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_TOPPER_INSTINCT_GUT_HEALTH_CHICKEN_14OZ": {
            "name": "Instinct Raw Boost Mixers Gut Health Chicken Recipe Freeze-Dried Dog Food Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_ACANA_CHICKEN_PATTIES_14OZ": {
            "name": "Acana Chicken Recipe Patties Freeze-Dried Dog Food & Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_ACANA_CHICKEN_MORSELS_8OZ": {
            "name": "Acana Chicken Recipe Morsels Freeze-Dried Dog Food & Topper, 8-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_ACANA_DUCK_PATTIES_14OZ": {
            "name": "Acana Duck Recipe Patties Freeze-Dried Dog Food & Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_ACANA_DUCK_MORSELS_8OZ": {
            "name": "Acana Duck Recipe Morsels Freeze-Dried Dog Food & Topper, 8-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_ACANA_TURKEY_PATTIES_14OZ": {
            "name": "Acana Turkey Recipe Patties Freeze-Dried Dog Food & Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_ACANA_TURKEY_MORSELS_8OZ": {
            "name": "Acana Turkey Recipe Morsels Freeze-Dried Dog Food & Topper, 8-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_ACANA_BEEF_PATTIES_14OZ": {
            "name": "Acana Beef Recipe Patties Freeze-Dried Dog Food & Topper, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_ACANA_BEEF_MORSELS_8OZ": {
            "name": "Acana Beef Recipe Morsels Freeze-Dried Dog Food & Topper, 8-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_BIXBI_CHICKEN_12OZ": {
            "name": "BIXBI Rawbble Chicken Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_BIXBI_CHICKEN_26OZ": {
            "name": "BIXBI Rawbble Chicken Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_BIXBI_BEEF_12OZ": {
            "name": "BIXBI Rawbble Beef Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_BIXBI_BEEF_26OZ": {
            "name": "BIXBI Rawbble Beef Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_BIXBI_PORK_12OZ": {
            "name": "BIXBI Rawbble Pork Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_BIXBI_PORK_26OZ": {
            "name": "BIXBI Rawbble Pork Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_BIXBI_TURKEY_12OZ": {
            "name": "BIXBI Rawbble Turkey Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_BIXBI_TURKEY_26OZ": {
            "name": "BIXBI Rawbble Turkey Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_BIXBI_SALMON_12OZ": {
            "name": "BIXBI Rawbble Salmon Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_BIXBI_SALMON_26OZ": {
            "name": "BIXBI Rawbble Salmon Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_BIXBI_LAMB_12OZ": {
            "name": "BIXBI Rawbble Lamb Recipe Freeze-Dried Dog Food, 12-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_BIXBI_LAMB_26OZ": {
            "name": "BIXBI Rawbble Lamb Recipe Freeze-Dried Dog Food, 26-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_DEHY_HK_WHOLE_GRAIN_CHICKEN_10LB": {
            "name": "The Honest Kitchen Whole Grain Chicken Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_DEHY_HK_WHOLE_GRAIN_BEEF_10LB": {
            "name": "The Honest Kitchen Whole Grain Beef Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_DEHY_HK_WHOLE_GRAIN_TURKEY_10LB": {
            "name": "The Honest Kitchen Whole Grain Turkey Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_DEHY_HK_GRAIN_FREE_CHICKEN_10LB": {
            "name": "The Honest Kitchen Grain-Free Chicken Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_DEHY_HK_GRAIN_FREE_BEEF_10LB": {
            "name": "The Honest Kitchen Grain-Free Beef Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_DEHY_HK_GRAIN_FREE_TURKEY_10LB": {
            "name": "The Honest Kitchen Grain-Free Turkey Dehydrated Dog Food, 10-lb box",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_SOJOS_COMPLETE_BEEF_7LB": {
            "name": "Sojos Complete Beef Recipe Freeze-Dried Raw Dog Food, 7-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_SOJOS_COMPLETE_TURKEY_7LB": {
            "name": "Sojos Complete Turkey Recipe Freeze-Dried Raw Dog Food, 7-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_SOJOS_COMPLETE_LAMB_8LB": {
            "name": "Sojos Complete Lamb Recipe Freeze-Dried Raw Dog Food, 8-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_SOJOS_MIX_A_MEAL_TURKEY_SALMON_7LB": {
            "name": "Sojos Mix-A-Meal Turkey & Salmon Dehydrated Raw Dog Food, 7-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_SOJOS_SIMPLY_BEEF_4OZ": {
            "name": "Sojos Simply Beef Freeze-Dried Dog Treats Topper, 4-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_SOJOS_GOATS_MILK_12OZ": {
            "name": "Sojos Goat's Milk Powder Dog Food Topper, 12-oz canister",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "CAT_AIRD_ZIWI_BEEF_2_2LB": {
            "name": "ZIWI Peak Beef Recipe Air-Dried Cat Food, 2.2-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "CAT_AIRD_ZIWI_LAMB_2_2LB": {
            "name": "ZIWI Peak Lamb Recipe Air-Dried Cat Food, 2.2-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "CAT_AIRD_ZIWI_MACKEREL_LAMB_2_2LB": {
            "name": "ZIWI Peak Mackerel & Lamb Recipe Air-Dried Cat Food, 2.2-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "CAT_AIRD_ZIWI_CHICKEN_2_2LB": {
            "name": "ZIWI Peak Chicken Recipe Air-Dried Cat Food, 2.2-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_VE_CHICKEN_NIBS_14OZ": {
            "name": "Vital Essentials Chicken Mini Nibs Freeze-Dried Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_VE_BEEF_NIBS_14OZ": {
            "name": "Vital Essentials Beef Mini Nibs Freeze-Dried Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_VE_DUCK_NIBS_14OZ": {
            "name": "Vital Essentials Duck Mini Nibs Freeze-Dried Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_VE_RABBIT_NIBS_14OZ": {
            "name": "Vital Essentials Rabbit Mini Nibs Freeze-Dried Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_VE_TURKEY_NIBS_14OZ": {
            "name": "Vital Essentials Turkey Mini Nibs Freeze-Dried Dog Food, 14-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_VE_MINNOWS_TREAT_1OZ": {
            "name": "Vital Essentials Freeze-Dried Minnows Dog & Cat Treat Topper, 1-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_DEHY_GL_CHICKEN_3LB": {
            "name": "Grandma Lucy's Artisan Chicken Freeze-Dried Dog Food, 3-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_DEHY_GL_PORK_3LB": {
            "name": "Grandma Lucy's Artisan Pork Freeze-Dried Dog Food, 3-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_DEHY_GL_LAMB_3LB": {
            "name": "Grandma Lucy's Artisan Lamb Freeze-Dried Dog Food, 3-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_DEHY_GL_VENISON_3LB": {
            "name": "Grandma Lucy's Artisan Venison Freeze-Dried Dog Food, 3-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_TOPPER_BB_CHICKEN_3OZ": {
            "name": "Blue Buffalo Wilderness Trail Toppers Wild Cuts Chicken in Gravy Dog Food Topper, 3-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_TOPPER_BB_DUCK_3OZ": {
            "name": "Blue Buffalo Wilderness Trail Toppers Wild Cuts Duck in Gravy Dog Food Topper, 3-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_TOPPER_BB_SALMON_3OZ": {
            "name": "Blue Buffalo Wilderness Trail Toppers Wild Cuts Salmon in Gravy Dog Food Topper, 3-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_RAW_NULO_TURKEY_DUCK_13OZ": {
            "name": "Nulo FreeStyle Freeze-Dried Raw Turkey & Duck Recipe Dog Food, 13-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_RAW_NULO_BEEF_13OZ": {
            "name": "Nulo FreeStyle Freeze-Dried Raw Beef Recipe Dog Food, 13-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_RAW_NULO_CHICKEN_SALMON_13OZ": {
            "name": "Nulo FreeStyle Freeze-Dried Raw Chicken & Salmon Recipe Dog Food, 13-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_K9_LAMB_FEAST_17_6OZ": {
            "name": "K9 Natural Lamb Feast Freeze-Dried Dog Food, 17.6-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_K9_BEEF_FEAST_17_6OZ": {
            "name": "K9 Natural Beef Feast Freeze-Dried Dog Food, 17.6-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_K9_CHICKEN_FEAST_17_6OZ": {
            "name": "K9 Natural Chicken Feast Freeze-Dried Dog Food, 17.6-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "CAT_TOPPER_TIKI_CHICKEN_1_5OZ": {
            "name": "Tiki Cat Born Carnivore Meal Topper Chicken Recipe, 1.5-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "CAT_TOPPER_TIKI_DUCK_1_5OZ": {
            "name": "Tiki Cat Born Carnivore Meal Topper Duck Recipe, 1.5-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "CAT_TOPPER_TIKI_SALMON_1_5OZ": {
            "name": "Tiki Cat Born Carnivore Meal Topper Salmon Recipe, 1.5-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_RAW_ORIJEN_ORIGINAL_16OZ": {
            "name": "Orijen Freeze-Dried Dog Food Original Recipe, 16-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_RAW_ORIJEN_REGIONAL_RED_16OZ": {
            "name": "Orijen Freeze-Dried Dog Food Regional Red Recipe, 16-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_RAW_ORIJEN_TUNDRA_16OZ": {
            "name": "Orijen Freeze-Dried Dog Food Tundra Recipe, 16-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_AIRD_EA_CHICKEN_1LB": {
            "name": "Earth Animal Wisdom Chicken Recipe Air-Dried Dog Food, 1-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "DOG_AIRD_EA_TURKEY_1LB": {
            "name": "Earth Animal Wisdom Turkey Recipe Air-Dried Dog Food, 1-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "DOG_AIRD_EA_BEEF_1LB": {
            "name": "Earth Animal Wisdom Beef Recipe Air-Dried Dog Food, 1-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "DOG_TOPPER_PUREBITES_DUCK_LIVER_2_2OZ": {
            "name": "PureBites Freeze-Dried Duck Liver Dog Treat Topper, 2.2-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_INFUSED_MERRICK_GREAT_PLAINS_RED_20LB": {
            "name": "Merrick Backcountry Raw Infused Grain-Free Great Plains Red Dry Dog Food, 20-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_INFUSED_MERRICK_BIG_GAME_20LB": {
            "name": "Merrick Backcountry Raw Infused Grain-Free Big Game Dry Dog Food, 20-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_INFUSED_MERRICK_PACIFIC_CATCH_20LB": {
            "name": "Merrick Backcountry Raw Infused Grain-Free Pacific Catch Dry Dog Food, 20-lb bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },
        "CAT_RAW_FELINE_CHICKEN_LAMB_11OZ": {
            "name": "Feline Natural Chicken & Lamb Freeze-Dried Cat Food, 11-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 19.99
        },
        "CAT_RAW_FELINE_BEEF_HOKI_11OZ": {
            "name": "Feline Natural Beef & Hoki Freeze-Dried Cat Food, 11-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 29.99
        },
        "CAT_RAW_FELINE_LAMB_11OZ": {
            "name": "Feline Natural Lamb Freeze-Dried Cat Food, 11-oz bag",
            "category": "Raw/Dehydrated/Topper",
            "price": 59.99
        },
        "DOG_TOPPER_SOLIDGOLD_BEEF_BONE_BROTH_8OZ": {
            "name": "Solid Gold NutrientBoost Beef Bone Broth Meal Topper, 8-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 79.99
        },
        "DOG_TOPPER_SOLIDGOLD_CHICKEN_BONE_BROTH_8OZ": {
            "name": "Solid Gold NutrientBoost Chicken Bone Broth Meal Topper, 8-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 99.99
        },
        "DOG_TOPPER_SOLIDGOLD_TURKEY_BONE_BROTH_8OZ": {
            "name": "Solid Gold NutrientBoost Turkey Bone Broth Meal Topper, 8-oz pouch",
            "category": "Raw/Dehydrated/Topper",
            "price": 129.99
        },


        "ACCESSORY_FRISCO_CRATE": {
            "name": "Frisco Fold & Carry Dog Crate",
            "category": "Accessories",
            "price": 44.99
        },
        "ACCESSORY_KONG_LEASH": {
            "name": "KONG Traffic Handle Dog Leash",
            "category": "Accessories",
            "price": 17.99
        },
        "ACCESSORY_PETSAFE_HARNESS": {
            "name": "PetSafe Easy Walk Dog Harness",
            "category": "Accessories",
            "price": 24.99
        },
        "WOOF_PUPSICLE_LL_DISPENSER_TOY_LARGE": {
            "name": "Woof Pupsicle Long Lasting Refillable Dog Treat Dispenser Toy, Large",
            "category": "Toys",
            "price": 9.99
        },
        "WOOF_PUPSICLE_PARTY_TREAT_TOY_PINK_SMALL": {
            "name": "Woof Party Pupsicle Treat Dispensing Dog Toy, Party Pink, Small",
            "category": "Toys",
            "price": 9.99
        },
        "NERF_SQUEAKER_CHECKER_BALL_BLUE_4IN": {
            "name": "Nerf Dog Squeaker Checker Ball Dog Toy, 4-in, Blue",
            "category": "Toys",
            "price": 9.99
        },
        "BENEBONE_BACON_PUPPY_CHEW_2CT": {
            "name": "Benebone Bacon Flavor Tough Puppy Chew Toy, 2 count",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_LAMBCHOP_PLUSH_REGULAR": {
            "name": "Multipet Lamb Chop Squeaky Plush Dog Toy, Regular",
            "category": "Toys",
            "price": 15.99
        },
        "KONG_FLOPPY_KNOTS_FOX_ML": {
            "name": "KONG Floppy Knots Dog Toy, Fox, Medium/Large",
            "category": "Toys",
            "price": 18.99
        },
        "WILDHARVEST_FRUIT_WOOD_CHEWS_5CT": {
            "name": "Wild Harvest Colored Fruit Flavored Wood Chews Small Pet Toy, 5 count",
            "category": "Toys",
            "price": 21.99
        },
        "CHUCKIT_ULTRA_BALL_MED_2PK": {
            "name": "Chuckit! Ultra Rubber Ball Tough Dog Toy, Medium, 2 pack",
            "category": "Toys",
            "price": 9.99
        },
        "BENEBONE_RUBBER_BONE_GREEN_MED": {
            "name": "Benebone Rubber Bone Dog Chew Toy, Green, Medium",
            "category": "Toys",
            "price": 9.99
        },
        "ZIPPYPAWS_SKINNY_PELTZ_3PK_LG": {
            "name": "ZippyPaws Skinny Peltz No Stuffing Squeaky Plush Dog Toys, 3-pack, Large",
            "category": "Toys",
            "price": 12.99
        },
        "FRISCO_COLORFUL_SPRINGS_10CT": {
            "name": "Frisco Colorful Springs Cat Toy, 10 count",
            "category": "Toys",
            "price": 15.99
        },
        "SUNGROW_COCONUT_FIBER_BALLS_3CT": {
            "name": "SunGrow Coconut Fiber Rabbit & Guinea Pigs Chew & Exercise Balls Teeth Grinding Treat, 3 count",
            "category": "Toys",
            "price": 18.99
        },
        "BENEBONE_WISHBONE_PB_LG": {
            "name": "Benebone Peanut Butter Flavor Wishbone Tough Dog Chew Toy, Large",
            "category": "Toys",
            "price": 21.99
        },
        "OUTWARD_HOUND_SKINZ_AVOCADO_MED": {
            "name": "Outward Hound Tough Skinz Durable Squeaky Stuffing-Free with Two Layers Dog Toy, Avocado, Medium",
            "category": "Toys",
            "price": 9.99
        },
        "OUTWARD_HOUND_DURABLEZ_BLUE_XL": {
            "name": "Outward Hound Durablez Tough Plush Dog Toy, Blue, X-Large",
            "category": "Toys",
            "price": 9.99
        },
        "FRISCO_FETCH_BALL_KNOT_SM": {
            "name": "Frisco Fetch Colorful Ball Knot Rope Dog Toy, Small/Medium",
            "category": "Toys",
            "price": 12.99
        },
        "NYLABONE_POWER_CHEW_RING_XL": {
            "name": "Nylabone Power Chew Textured Dog Chew Ring Toy Flavor Medley, X-Large",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_GUMBY_PLUSH": {
            "name": "Multipet Gumby Plush Squeaky Dog Toy",
            "category": "Toys",
            "price": 18.99
        },
        "KONG_PLUSH_DUCK_SM": {
            "name": "KONG Plush Duck Dog Toy, Small",
            "category": "Toys",
            "price": 21.99
        },
        "SUPERBIRD_BIRDIE_BALL_XL": {
            "name": "Super Bird Creations Birdie Ball Exercise Bird Toy, X-Large",
            "category": "Toys",
            "price": 9.99
        },
        "CHUCKIT_ULTRA_DUO_TUG_MED": {
            "name": "Chuckit! Ultra Duo Tug Tough Dog Toy, Medium",
            "category": "Toys",
            "price": 9.99
        },
        "ALLFORPAWS_MOTION_BALL_BLUE_3_3IN": {
            "name": "allforpaws Motion Activated Ball Dog Toy, Blue, 3.3-in",
            "category": "Toys",
            "price": 12.99
        },
        "LOVELY_CAVES_INTERACTIVE_BALL_ORANGE": {
            "name": "Lovely Caves Interactive Cat Ball Cat Toy with Tail, Orange",
            "category": "Toys",
            "price": 15.99
        },
        "FRISCO_PEAPOD_PEAS_PLUSH_SM": {
            "name": "Frisco Peapod & Peas 2-in-1 Rip for Surprise Plush Squeaky Dog Toy, Small",
            "category": "Toys",
            "price": 18.99
        },
        "RUFFINIT_MALLARD_PLUSH": {
            "name": "RUFFIN' IT Woodlands Mallard Plush Dog Toy",
            "category": "Toys",
            "price": 21.99
        },
        "PETSTAGES_ORKA_DENTAL_LINKS": {
            "name": "Petstages Orka Dental Links Tough Dog Chew Toy",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_LOOFA_ORIG_PLUSH_SM": {
            "name": "Multipet Loofa Dog The Original Squeaky Plush Dog Toy, Color Varies, Small",
            "category": "Toys",
            "price": 9.99
        },
        "KONG_WUBBA_CLASSIC_LG": {
            "name": "KONG Wubba Classic Dog Toy, Color Varies, Large",
            "category": "Toys",
            "price": 12.99
        },
        "ROSEWOOD_FUN_BALLS_3CT": {
            "name": "Naturals by Rosewood Trio of Fun Balls Small Pet Toy, 3 count",
            "category": "Toys",
            "price": 15.99
        },
        "CHUCKIT_ULTRA_FETCH_STICK": {
            "name": "Chuckit! Ultra Fetch Stick Dog Toy",
            "category": "Toys",
            "price": 18.99
        },
        "SMARTYKAT_HOT_PURSUIT_BLUE": {
            "name": "SmartyKat Hot Pursuit Electronic Concealed Motion Cat Toy, Blue",
            "category": "Toys",
            "price": 21.99
        },
        "NYLABONE_CHEESE_MED": {
            "name": "Nylabone Power Chew Cheese Dog Toy, Medium",
            "category": "Toys",
            "price": 9.99
        },
        "FRISCO_HIPPO_PLUSH_ML": {
            "name": "Frisco Hippo Textured Plush Squeaky Dog Toy, Medium/Large",
            "category": "Toys",
            "price": 9.99
        },
        "NOCCIOLA_ZOO_SERIES_5CT": {
            "name": "Nocciola Zoo Series with Strange Squeaky 5 Different Funny Sounds Dog Plush Toy, 5 count",
            "category": "Toys",
            "price": 12.99
        },
        "NECOICHI_SCRATCHER_WALL_REG": {
            "name": "Necoichi Premium Comfort Cat Scratcher Wall, Dark Cherry/Brown, Regular",
            "category": "Toys",
            "price": 15.99
        },
        "RUFFINIT_SQUIRREL_PLUSH": {
            "name": "RUFFIN' IT Woodlands Squirrel Plush Dog Toy",
            "category": "Toys",
            "price": 18.99
        },
        "SUNGROW_BOREDOM_RELIEF_TOY": {
            "name": "SunGrow Boredom & Separation Anxiety Relief Stimulation Treat Dispensing Cat & Dog Toy",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_LATEX_GLOBLET_PIG_4IN": {
            "name": "Multipet Latex Polka Dot Globlet Squeaky Pig Dog Toy, Color Varies, 4-in, 1 count",
            "category": "Toys",
            "price": 9.99
        },
        "KONG_SQUEAKAIR_BALLS_SM": {
            "name": "KONG Squeakair Balls Packs Dog Toy, Small",
            "category": "Toys",
            "price": 9.99
        },
        "GRIGGLES_HAPPY_SMILE": {
            "name": "Griggles Happy Smile Squeaker Dog Chew Toy",
            "category": "Toys",
            "price": 12.99
        },
        "CHUCKIT_INDOOR_BALL": {
            "name": "Chuckit! Indoor Ball Dog Toy",
            "category": "Toys",
            "price": 15.99
        },
        "FRISCO_BIRD_FEATHERS_WAND": {
            "name": "Frisco Bird with Feathers Teaser Wand Cat Toy with Catnip, Blue",
            "category": "Toys",
            "price": 18.99
        },
        "NYLABONE_EASY_HOLD_BACON_LG": {
            "name": "Nylabone Power Chew Easy-Hold Dog Dental Chew Toy Easy Hold Bacon, Large",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_CRUNCHY_GRAPES_XL": {
            "name": "A&E Cage Company Crunchy Grapes Preening Bird Toy, X-Large",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_CANDIES_LOOFAH": {
            "name": "A&E Cage Company Candies Loofah Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_PIXEL_CUBE": {
            "name": "A&E Cage Company Pixel Cube Preening Bird Toy",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_STARBURST": {
            "name": "A&E Cage Company Starburst Preening Bird Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_WOOD_CYLINDER_BALL": {
            "name": "A&E Cage Company Wooden Cylinder & Ball Chew Small Pet Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_STAR_SHRED_SEEK": {
            "name": "A&E Cage Company Star Shred & Seek Preening Bird Toy",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_BEAK_TOSS_BONANZA": {
            "name": "A&E Cage Company Beak Toss Bonanaza Exercise Bird Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_NIBBLES_RING_3PC": {
            "name": "A&E Cage Company Nibbles Chew Ring 3pc Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_SWEET_TWEETS_CUPCAKE": {
            "name": "A&E Cage Company Sweet Tweets Cupcake Foraging Bird Toy",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_RAINBOW_BOING": {
            "name": "A&E Cage Company Rainbow Cotton Rope Boing Bird Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_NIBBLES_APPLE": {
            "name": "A&E Cage Company Nibbles Foraging Apple Small Pet Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_NIBBLES_ICECREAM": {
            "name": "A&E Cage Company Nibbles Ice Cream Small Pet Toy",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_TWEETING_TALLY": {
            "name": "A&E Cage Company Tweeting Tally Cruncher Chew Bird Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_NIBBLES_GARDEN_KNOB": {
            "name": "A&E Cage Company Nibbles Garden Knob Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_SHRED_O_MANIA": {
            "name": "A&E Cage Company Shred-O-Mania Foraging Bird Toy",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_BEAK_BOARD": {
            "name": "A&E Cage Company Beak Board Exercise Bird Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_TINY_RINGS_STARS": {
            "name": "A&E Cage Company Tiny Rings & Stars Bird Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_PRESENT_SHREDDER": {
            "name": "A&E Cage Company Present Shredder Preening Bird Toy",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_NIBBLES_HAY_TUBE": {
            "name": "A&E Cage Company Nibbles Hay Tube Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_SPLASH_CLEAN": {
            "name": "A&E Cage Company Splash n' Clean Exercise Bird Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_SOFT_TENT": {
            "name": "A&E Cage Company Soft Sided Bird Tent, Pattern Varies",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_POPCORN_LOOFAH": {
            "name": "A&E Cage Company Popcorn Loofah Small Pet Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_STARBURST_TOY": {
            "name": "A&E Cage Company Starburst Bird Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_RIPPIN_RAINBOW": {
            "name": "A&E Cage Company Rippin Rainbow Chew Bird Toy",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_FRUITS_LOOFAH": {
            "name": "A&E Cage Company Bunch of Fruits Loofah Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_SILLY_LINKS": {
            "name": "A&E Cage Company Silly Links Bird Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_BLOCK_CRAZE": {
            "name": "A&E Cage Company Block Craze Chew Bird Toy",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_WRAP_N_ROLLS": {
            "name": "A&E Cage Company Wrap N Rolls Exercise Bird Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_NIBBLES_RAINBOW_FISH": {
            "name": "A&E Cage Company Nibbles Rainbow Fish Small Pet Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_KEET_RINGS": {
            "name": "A&E Cage Company Keet Rings Bird Toy",
            "category": "Toys",
            "price": 21.99
        },
        "AECAGE_EGG_STRAVAGANZA": {
            "name": "A&E Cage Company Egg-Stravaganza Bird Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_NIBBLES_LOVE_ROSE": {
            "name": "A&E Cage Company Nibbles Love U Bunches Rose Small Pet Toy",
            "category": "Toys",
            "price": 9.99
        },
        "AECAGE_NIBBLES_BUNNY_CARROT": {
            "name": "A&E Cage Company Nibbles Bunny/Carrot Box Small Pet Toy",
            "category": "Toys",
            "price": 12.99
        },
        "AECAGE_NIBBLES_VINE_BALL": {
            "name": "A&E Cage Company Nibbles Vine Ball on String Small Pet Toy",
            "category": "Toys",
            "price": 15.99
        },
        "AECAGE_HOT_FLAMES": {
            "name": "A&E Cage Company Hot Flames Preening Bird Toy",
            "category": "Toys",
            "price": 18.99
        },
        "AECAGE_SUSHI_SHREDDER": {
            "name": "A&E Cage Company Sushi Shredder Foraging Bird Toy",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_BOUNCY_BURROW_BABIES": {
            "name": "Multipet Bouncy Burrow Buddies Babies Squeaky Stuffing-Free Plush Puppy Toy, Character Varies",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_NOBBLY_WOBBLY_3IN": {
            "name": "Multipet Nobbly Wobbly Ball Dog Toy, Color Varies, 3-in",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_GUMBY_RUBBER": {
            "name": "Multipet Gumby Rubber Dog Toy",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_KITTY_CARPET_16IN": {
            "name": "Multipet Sweet Spot Kitty Carpet Summers Dream Plush Cat Toy with Catnip, Multicolor, 16-in",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_NUTS_KNOTS_ROPE": {
            "name": "Multipet Nuts for Knots Rope Tug & Danglers Dog Toy, Color Varies, 1 count",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_LOOFA_LIGHT_SM": {
            "name": "Multipet Loofa Light-Weight Squeaky Stuffing-Free Dog Toy, Color Varies, Small",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_BDAY_CAKE_SLICE": {
            "name": "Multipet Birthday Cake Slice Plush Cat Toy with Catnip, 4.5-in, Blue/White",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_LOOFA_LATEX_12IN": {
            "name": "Multipet Loofa Latex Squeaky Dog Toy, Color Varies, 12-in, 1 count",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_MR_BILL_PLUSH": {
            "name": "Multipet Mr. Bill Plush Dog Toy",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_AROMADOG_MAN": {
            "name": "Multipet Aromadog Man Therapeutic Essential Oil Squeaky Plush Dog Toy, Style Varies, 1 count",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_PAUL_FRANK_JULIUS": {
            "name": "Multipet Paul Frank Julius Squeaky Plush Dog Toy, Brown, 12-in",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_MUSICAL_BDAY_CAKE": {
            "name": "Multipet Musical Birthday Cake Plush Dog Toy",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_PARROT_WAND_40IN": {
            "name": "Multipet Margaritaville Parrot Wand Cat Toy with Red Bird, Multicolor, 40-in",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_KATZ_KUDDLERZ": {
            "name": "Multipet Katz Kuddlerz Plush Cat Toy, Assorted Colors",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_CATERPILLAR_18IN": {
            "name": "Multipet Eric Carle Hungry Caterpillar Dog Toy, Multicolor, 18-in",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_MALLARD_PLUSH_LG": {
            "name": "Multipet Migrator Bird Mallard Squeaky Plush Dog Toy, Large",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_VALUE_PACK_24": {
            "name": "Multipet Value Pack Cat Toy, Assorted Colors, 24-pack",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_CLEAN_MINT_ROPE": {
            "name": "Multipet Canine Clean Mint Rope & Balls Tough Dog Chew Toy, Blue",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_GUMBY_ROPE_10IN": {
            "name": "Multipet Gumby Squeaky Plush Dog Toy with Rope Arms, Green, 10-in",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_MARGARITA_GLASS_8IN": {
            "name": "Multipet Margaritaville Margarita Glass Squeaky Plush Dog Toy, Blue, 8-in",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_MARGARITA_SALT_LIME": {
            "name": "Multipet Margaritaville Margarita/Salt/Lime Plush Cat Toy with Catnip, Multicolor, 5.25-in",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_SPIKE_TPR_BALL": {
            "name": "Multipet Spike TPR Ball Dog Toy, Color Varies",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_KNOBBY_KNITS": {
            "name": "Multipet Knobby Knits Cat Toy, Character Varies",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_CARDBOARD_ROLLER_9_5IN": {
            "name": "Multipet Cardboard Roller Cat Scratcher Toy with Catnip, Color Varies, 9.5-in, 1 count",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_LOOK_TALKING_FROG": {
            "name": "Multipet Look Who's Talking Plush Cat Toy with Catnip, Frog",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_LOOFA_PLUSH_CAT": {
            "name": "Multipet Loofa Plush Cat Toy with Catnip, Color Varies",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_SILVERVINE_BAG": {
            "name": "Multipet Catnip Garden Silvervine Cat Toy with Catnip, White, 1-oz bag",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_AROMADOG_PUPPY": {
            "name": "Multipet Aromadog Theraputic Essential Oil Squeaky Plush Puppy Toy, Character Varies, 1 count",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_MICE_3_PATTERN": {
            "name": "Multipet Margaritaville Mice 3 Pattern Plush Cat Toy with Catnip, Multicolor, 4.25-in",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_MR_BILL_CAT": {
            "name": "Multipet Mr. Bill Plush Cat Toy with Catnip",
            "category": "Toys",
            "price": 21.99
        },
        "MULTIPET_BDAY_PRESENT_2_25IN": {
            "name": "Multipet Birthday Present Plush Cat Toy with Catnip, Pink/White, 2.25-in",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_CLEAN_MINT_BONE": {
            "name": "Multipet Canine Clean Mint Bone Tough Dog Chew Toy, Blue",
            "category": "Toys",
            "price": 9.99
        },
        "MULTIPET_LOBBERZ_FISH": {
            "name": "Multipet Lobberz Fish Squeaky Dog Toy, Color Varies",
            "category": "Toys",
            "price": 12.99
        },
        "MULTIPET_FLIP_FLOP_4IN": {
            "name": "Multipet Margaritaville Flip Flop Plush Cat Toy with Catnip, Blue, 4-in",
            "category": "Toys",
            "price": 15.99
        },
        "MULTIPET_KNOBBY_NOGGINS": {
            "name": "Multipet Knobby Noggins Squeaky Plush Dog Toy, Character Varies",
            "category": "Toys",
            "price": 18.99
        },
        "MULTIPET_ORIGAMI_PALS_8IN": {
            "name": "Multipet Origami Pals Squeaky Dog Toy, Color Varies, 8-in, 1 count",
            "category": "Toys",
            "price": 21.99
        },

        "ACCESSORY_RUFFWEAR_OUTDOOR_GEAR": {
            "name": "Ruffwear Front Range Dog Harness",
            "category": "Accessories",
            "price": 39.99
        },
        "ACCESSORY_KURGO_CAR_SEAT_COVER": {
            "name": "Kurgo Car Seat Cover",
            "category": "Accessories",
            "price": 49.99
        },
        "ACCESSORY_BLUEBERRY_PET_COLLAR": {
            "name": "Blueberry Pet Dog Collar",
            "category": "Accessories",
            "price": 14.99
        },
        "ACCESSORY_MIDWEST_EXERCISE_PEN": {
            "name": "MidWest Exercise Pen",
            "category": "Accessories",
            "price": 39.99
        },
        "ACCESSORY_CARLSON_PET_GATE": {
            "name": "Carlson Pet Gate with Door",
            "category": "Gates & Pens",
            "price": 44.99
        },
        "ACCESSORY_OUTWARD_HOUND_LIFE_JACKET": {
            "name": "Outward Hound Granby Dog Life Jacket",
            "category": "Accessories",
            "price": 24.99
        },
        "ACCESSORY_NYLABONE_DURABLE_CHEW": {
            "name": "Nylabone Durable Chew Toy",
            "category": "Dog Toys",
            "price": 9.99
        },
        "ACCESSORY_EARTH_RATED_WASTE_BAGS": {
            "name": "Earth Rated Dog Waste Bags",
            "category": "Cleaning/Potty",
            "price": 5.99
        },
        "ACCESSORY_FURHAVEN_BED": {
            "name": "FurHaven Orthopedic Pet Bed",
            "category": "Beds & Furniture",
            "price": 32.99
        },
        "ACCESSORY_SNOOZER_CAR_SEAT": {
            "name": "Snoozer Lookout Car Seat",
            "category": "Car Travel",
            "price": 59.99
        },
        "ACCESSORY_KH_HEATED_BED": {
            "name": "K&H Pet Products Heated Pet Bed",
            "category": "Beds & Furniture",
            "price": 49.99
        },
        "ACCESSORY_ZIPPYPAWS_PLUSH_TOY": {
            "name": "ZippyPaws Plush Squeaker Toy",
            "category": "Dog Toys",
            "price": 7.99
        },
        "ACCESSORY_DOG_GONE_SMART_DOORMAT": {
            "name": "Dog Gone Smart Dirty Dog Doormat",
            "category": "Home & Living",
            "price": 19.99
        },
        "ACCESSORY_RED_DINGO_ID_TAG": {
            "name": "Red Dingo Engraved Pet ID Tag",
            "category": "Accessories",
            "price": 12.99
        },
        "ACCESSORY_HAMILTON_COLLAR": {
            "name": "Hamilton Adjustable Dog Collar",
            "category": "Accessories",
            "price": 9.99
        },
        "ACCESSORY_FLEXI_RETRACTABLE_LEASH": {
            "name": "Flexi Retractable Dog Leash",
            "category": "Accessories",
            "price": 18.99
        },
        "ACCESSORY_HALTI_HEADCOLLAR": {
            "name": "Halti Headcollar for Dogs",
            "category": "Accessories",
            "price": 14.99
        },
        "ACCESSORY_ANDIS_GROOMING_CLIPPER": {
            "name": "Andis UltraEdge Dog Grooming Clipper",
            "category": "Grooming",
            "price": 79.99
        },
        "ACCESSORY_WAHL_GROOMING_CLIPPER": {
            "name": "Wahl Professional Pet Clipper Kit",
            "category": "Grooming",
            "price": 59.99
        },
        "ACCESSORY_FURMINATOR_DESHED_DOG": {
            "name": "FURminator Deshedding Tool for Dogs",
            "category": "Grooming",
            "price": 24.99
        },

        "MISC_PETALIVE_HERBAL_SUPPLEMENT": {
            "name": "PetAlive Herbal Homeopathic Supplement",
            "category": "Supplements",
            "price": 21.99
        },
        "MISC_BURTS_BEES_DOG_SHAMPOO": {
            "name": "Burt’s Bees Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "MISC_VETS_BEST_SHAMPOO": {
            "name": "Vet’s Best Hypo-Allergenic Shampoo",
            "category": "Grooming/Health",
            "price": 8.99
        },
        "MISC_SENTRY_CALMING_AID": {
            "name": "Sentry Calming Pheromone Spray",
            "category": "Calming Aids",
            "price": 14.99
        },
        "MISC_THUNDERSHIRT_DOG": {
            "name": "ThunderShirt Classic Dog Anxiety Jacket",
            "category": "Calming Apparel",
            "price": 39.99
        },
        "MISC_SERESTO_FLEA_TICK_DOG": {
            "name": "Seresto Flea & Tick Collar for Dogs",
            "category": "Flea & Tick",
            "price": 57.99
        },
        "MISC_ADAMS_FLEA_TICK_SOLUTION": {
            "name": "Adams Flea & Tick Home Spray",
            "category": "Flea & Tick",
            "price": 12.99
        },
        "MISC_ARM_HAMMER_ODOR_REMOVER": {
            "name": "Arm & Hammer Pet Stain & Odor Remover",
            "category": "Cleaning & Odor Control",
            "price": 7.99
        },
        "MISC_NATURES_MIRACLE_STAIN_ODOR": {
            "name": "Nature’s Miracle Stain & Odor Remover",
            "category": "Cleaning & Odor Control",
            "price": 8.99
        },
        "MISC_PLANET_DOG_TOY": {
            "name": "Planet Dog Orbee-Tuff Ball",
            "category": "Dog Toys",
            "price": 11.99
        },
        "MISC_BENEBONE_CHEW_TOY": {
            "name": "Benebone Wishbone Durable Chew Toy",
            "category": "Dog Toys",
            "price": 12.99
        },
        "MISC_ZESTY_PAWS_SUPPLEMENT": {
            "name": "Zesty Paws Multifunctional Supplement",
            "category": "Supplements",
            "price": 26.99
        },
        "MISC_ARK_NATURALS_DENTAL": {
            "name": "Ark Naturals Brushless Toothpaste Chews",
            "category": "Dental Chews",
            "price": 13.99
        },
        "MISC_FRONTLINE_FLEA_TICK": {
            "name": "Frontline Plus Flea & Tick Treatment",
            "category": "Flea & Tick",
            "price": 39.99
        },
        "MISC_ADVANTAGE_FLEA_TICK": {
            "name": "Advantage II Flea Treatment",
            "category": "Flea & Tick",
            "price": 37.99
        },
        "MISC_K9_ADVANTIX_FLEA_TICK": {
            "name": "K9 Advantix II Flea & Tick Treatment",
            "category": "Flea & Tick",
            "price": 42.99
        },
        "MISC_BIO_GROOM_SHAMPOO": {
            "name": "Bio-Groom Pet Shampoo",
            "category": "Grooming",
            "price": 8.99
        },
        
        "DOG_DRY_FOOD_7.7_LBS": {
            "name": "Dog Dry Food 7.7 lbs",
            "category": "Dog Food (Non-Prescription)",
            "price": 18.99
        },
        "DOG_DRY_FOOD_15.5_LBS": {
            "name": "Dog Dry Food 15.5 lbs",
            "category": "Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DRY_FOOD_25.5_LBS": {
            "name": "Dog Dry Food 25.5 lbs",
            "category": "Dog Food (Non-Prescription)",
            "price": 45.99
        },
        "CAT_DRY_FOOD_4.4_LBS": {
            "name": "Cat Dry Food 4.4 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 12.99
        },
        "CAT_DRY_FOOD_12.2_LBS": {
            "name": "Cat Dry Food 12.2 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 22.99
        },
        "CAT_DRY_FOOD_19.8_LBS": {
            "name": "Cat Dry Food 19.8 lbs",
            "category": "Cat Food (Non-Prescription)",
            "price": 34.99
        },
        "DOG_CANS_12.5OZ_CASE12": {
            "name": "Dog Canned Food 12.5 oz (Case of 12)",
            "category": "Dog Food (Non-Prescription)",
            "price": 25.99
        },
        "DOG_CANS_12.5OZ_CASE24": {
            "name": "Dog Canned Food 12.5 oz (Case of 24)",
            "category": "Dog Food (Non-Prescription)",
            "price": 47.99
        },
        "CAT_CANS_5.5OZ_CASE24": {
            "name": "Cat Canned Food 5.5 oz (Case of 24)",
            "category": "Cat Food (Non-Prescription)",
            "price": 29.99
        },
        "CAT_CANS_5.5OZ_CASE12": {
            "name": "Cat Canned Food 5.5 oz (Case of 12)",
            "category": "Cat Food (Non-Prescription)",
            "price": 15.99
        },
        "DOG_TREAT_BISCUIT": {
            "name": "Dog Treat - Biscuit",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.99
        },
        "DOG_TREAT_JERKY": {
            "name": "Dog Treat - Jerky",
            "category": "Dog Treats (Non-Prescription)",
            "price": 12.50
        },
        "DOG_DENTAL_TREAT": {
            "name": "Dog Dental Treat",
            "category": "Dog Treats (Non-Prescription)",
            "price": 14.99
        },
        "CAT_TREAT_CRUNCHY": {
            "name": "Cat Treat - Crunchy",
            "category": "Cat Treats (Non-Prescription)",
            "price": 6.99
        },
        "CAT_TREAT_SOFT": {
            "name": "Cat Treat - Soft",
            "category": "Cat Treats (Non-Prescription)",
            "price": 7.99
        },
        "DOG_COLLAR_LARGE": {
            "name": "Dog Collar - Large",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_LEASH_DURABLE": {
            "name": "Dog Leash - Durable",
            "category": "Accessories",
            "price": 14.99
        },
        "CAT_HARNESS": {
            "name": "Cat Harness",
            "category": "Accessories",
            "price": 12.99
        },
        "LARGE_DOG_CRATE": {
            "name": "Large Dog Crate",
            "category": "Crates & Kennels",
            "price": 129.99
        },
        "CAT_TREE_DELUXE": {
            "name": "Cat Tree Deluxe",
            "category": "Cat Trees & Towers",
            "price": 179.99
        },
        "HORSE_FEED_BAG": {
            "name": "Horse Feed 50 lbs",
            "category": "Horse & Farm",
            "price": 59.99
        },
        "FRESHWATER_AQUARIUM_50GAL": {
            "name": "Freshwater Aquarium 50 Gallon",
            "category": "Fish & Aquatic Supplies",
            "price": 249.99
        },

        "DOG_RAW_FREEZE_DRIED": {
            "name": "Dog Raw Freeze-Dried Patties",
            "category": "Dog Food (Non-Prescription)",
            "price": 29.99
        },
        "DOG_DEHYDRATED_FOOD": {
            "name": "Dog Dehydrated Food Mix",
            "category": "Dog Food (Non-Prescription)",
            "price": 36.99
        },
        "DOG_FRESH_FOOD_ROLL": {
            "name": "Dog Fresh Food Roll",
            "category": "Dog Food (Non-Prescription)",
            "price": 19.99
        },
        "DOG_FOOD_TOPPER_BONE_BROTH": {
            "name": "Dog Food Topper - Bone Broth",
            "category": "Food Toppers & Meal Enhancers",
            "price": 6.99
        },

        "DOG_TREAT_SOFT_CHEWY": {
            "name": "Dog Treat - Soft & Chewy",
            "category": "Dog Treats (Non-Prescription)",
            "price": 8.49
        },
        "DOG_TREAT_MEAT_STRIPS": {
            "name": "Dog Treat - Meat Strips",
            "category": "Dog Treats (Non-Prescription)",
            "price": 11.49
        },
        "DOG_TREAT_LONG_LASTING_BULLY": {
            "name": "Dog Long-Lasting Bully Stick",
            "category": "Dog Treats (Non-Prescription)",
            "price": 5.99
        },
        "DOG_TREAT_TRAINING_BITES": {
            "name": "Dog Training Treats (Bite-Sized)",
            "category": "Dog Treats (Non-Prescription)",
            "price": 5.49
        },

        "DOG_TOY_PLUSH": {
            "name": "Dog Toy - Plush Squeaker",
            "category": "Dog Toys",
            "price": 7.99
        },
        "DOG_TOY_PUZZLE": {
            "name": "Dog Interactive Puzzle Toy",
            "category": "Dog Toys",
            "price": 14.99
        },
        "DOG_TOY_RUBBER_CHEW": {
            "name": "Dog Chew Toy (Durable Rubber)",
            "category": "Dog Toys",
            "price": 9.99
        },
        "DOG_TOY_FETCH_BALL": {
            "name": "Dog Fetch Ball",
            "category": "Dog Toys",
            "price": 4.99
        },

        "DOG_HARNESS_NOPULL": {
            "name": "Dog Harness - No Pull",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_ID_TAG_CUSTOM": {
            "name": "Dog ID Tag (Custom Engraving)",
            "category": "Accessories",
            "price": 9.49
        },
        "DOG_COAT_WATERPROOF": {
            "name": "Dog Waterproof Coat",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_BED_ORTHOPEDIC": {
            "name": "Dog Orthopedic Bed",
            "category": "Accessories",
            "price": 59.99
        },
        "DOG_CAR_SEAT_COVER": {
            "name": "Dog Car Seat Cover",
            "category": "Accessories",
            "price": 34.99
        },
        "DOG_GROOMING_SHAMPOO": {
            "name": "Dog Shampoo - Oatmeal",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_ENZYME_CLEANER": {
            "name": "Dog Enzyme Cleaner",
            "category": "Cleaning & Potty",
            "price": 10.99
        },
        "DOG_SLOW_FEED_BOWL": {
            "name": "Dog Slow Feed Bowl",
            "category": "Bowls & Feeders",
            "price": 12.99
        },

        "DOG_VITAMIN_JOINT_SUPPORT": {
            "name": "Dog Joint Support Supplement",
            "category": "Dog Health & Wellness",
            "price": 19.99
        },
        "DOG_FLEA_TICK_COLLAR": {
            "name": "Dog Flea & Tick Collar (OTC)",
            "category": "Dog Health & Wellness",
            "price": 24.99
        },
        "DOG_DEWORMER_BASIC": {
            "name": "Dog Dewormer (Broad Spectrum, OTC)",
            "category": "Dog Health & Wellness",
            "price": 14.99
        },
        "DOG_FIRST_AID_SPRAY": {
            "name": "Dog First Aid Antiseptic Spray",
            "category": "Dog Health & Wellness",
            "price": 7.99
        },
        "DOG_DENTAL_RINSE": {
            "name": "Dog Dental Rinse",
            "category": "Dog Health & Wellness",
            "price": 10.99
        },

        "CAT_FOOD_RAW_FREEZE_DRIED": {
            "name": "Cat Raw Freeze-Dried Morsels",
            "category": "Cat Food (Non-Prescription)",
            "price": 21.99
        },
        "CAT_FOOD_DEHYDRATED": {
            "name": "Cat Dehydrated Food Mix",
            "category": "Cat Food (Non-Prescription)",
            "price": 27.99
        },
        "CAT_FOOD_TOPPER_GRAVY": {
            "name": "Cat Food Topper - Savory Gravy",
            "category": "Food Toppers & Meal Enhancers",
            "price": 5.99
        },

        "CAT_TREAT_FREEZEDRIED_SALMON": {
            "name": "Cat Treat - Freeze-Dried Salmon",
            "category": "Cat Treats (Non-Prescription)",
            "price": 8.99
        },
        "CAT_DENTAL_TREAT_GREENIES": {
            "name": "Cat Dental Treat - Greenies",
            "category": "Cat Treats (Non-Prescription)",
            "price": 6.99
        },
        "CAT_GRASS_KIT": {
            "name": "Cat Grass Kit",
            "category": "Cat Treats/Enrichment",
            "price": 4.99
        },

        "CAT_LITTER_DRELSEYS_ULTRA_40LB": {
            "name": "Dr. Elsey's Ultra Unscented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_DRELSEYS_ULTRA_20LB": {
            "name": "Dr. Elsey's Ultra Unscented Clumping Clay Cat Litter, 20-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_DRELSEYS_CATATTRACT_40LB": {
            "name": "Dr. Elsey's Cat Attract Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_DRELSEYS_CATATTRACT_20LB": {
            "name": "Dr. Elsey's Cat Attract Clumping Clay Cat Litter, 20-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_DRELSEYS_PAWSENSITIVE_20LB": {
            "name": "Dr. Elsey's Paw Sensitive Clumping Clay Cat Litter, 20-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_DRELSEYS_RR_STRESS_20LB": {
            "name": "Dr. Elsey's R&R Stress-Reducing Clumping Clay Cat Litter, 20-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_WB_MULTI_UNSC_8LB": {
            "name": "World’s Best Multi-Cat Unscented Clumping Corn Cat Litter, 8-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_WB_MULTI_UNSC_15LB": {
            "name": "World’s Best Multi-Cat Unscented Clumping Corn Cat Litter, 15-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_WB_MULTI_UNSC_28LB": {
            "name": "World’s Best Multi-Cat Unscented Clumping Corn Cat Litter, 28-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_WB_COMFORTCARE_28LB": {
            "name": "World’s Best Comfort Care Unscented Clumping Corn Litter, 28-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_WB_LOWTRACK_15LB": {
            "name": "World’s Best Low Tracking & Dust Control Multiple Cat Litter, 15-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_WB_LAVENDER_15LB": {
            "name": "World’s Best Lavender Scented Clumping Corn Cat Litter, 15-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_TIDYCATS_FREECLEAN_17LB": {
            "name": "Purina Tidy Cats Free & Clean Lightweight Unscented Clumping Clay Cat Litter, 17-lb box",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_TIDYCATS_LW_24_7_17LB": {
            "name": "Purina Tidy Cats Lightweight 24/7 Scented Clumping Clay Cat Litter, 17-lb box",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_TIDYCATS_24_7_PERF_40LB": {
            "name": "Purina Tidy Cats 24/7 Performance Scented Non-Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_AH_MULTICAT_CLEANBURST_40LB": {
            "name": "Arm & Hammer Multi-Cat Strength Clean Burst Clumping Litter, 40-lb box",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_AH_CLUMPSEAL_14LB": {
            "name": "Arm & Hammer Clump & Seal Multi-Cat Scented Clumping Clay Cat Litter, 14-lb box",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_AH_SLIDE_38LB": {
            "name": "Arm & Hammer Slide Multi-Cat Scented Clumping Clay Cat Litter, 38-lb box",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_AH_SUPERSCOOP_UNSC_40LB": {
            "name": "Arm & Hammer Super Scoop Unscented Clumping Clay Cat Litter, 40-lb box",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_FS_SIMPLY_UNSC_14LB": {
            "name": "Fresh Step Simply Unscented Clumping Clay Cat Litter, 14-lb box",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_FS_MULTICAT_EXTRA_25LB": {
            "name": "Fresh Step Multi-Cat Extra Strength Scented Clumping Cat Litter, 25-lb box",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_FS_TRIPLEACTION_15_4LB": {
            "name": "Fresh Step Triple Action Scented Clumping Clay Cat Litter, 15.4-lb box",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_FS_PREMIUM_SCENTED_35LB": {
            "name": "Fresh Step Premium Scented Non-Clumping Cat Litter, 35-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_FS_CRYSTALS_SCENTED_8LB": {
            "name": "Fresh Step Crystals Scented Non-Clumping Cat Litter, 8-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_FRISCO_MULTI_UNSC_40LB": {
            "name": "Frisco Multi-Cat Unscented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_FRISCO_MULTI_FRESH_40LB": {
            "name": "Frisco Multi-Cat Fresh Scented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_FRISCO_MULTI_UNSC_20LB": {
            "name": "Frisco Multi-Cat Unscented Clumping Clay Cat Litter, 20-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_FRISCO_BAKINGSODA_40LB": {
            "name": "Frisco Multi-Cat Baking Soda Unscented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_FRISCO_LAVENDER_40LB": {
            "name": "Frisco Lavender Fields Scented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_FRISCO_ATTRACTANT_40LB": {
            "name": "Frisco Attractant Multi-Cat Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_FRISCO_TROPICAL_40LB": {
            "name": "Frisco Tropical Breeze Scented Clumping Clay Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_FRISCO_PINEPELLET_40LB": {
            "name": "Frisco Pine Pellet Unscented Non-Clumping Wood Cat Litter, 40-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_NATFRESH_WALNUT_14LB": {
            "name": "Naturally Fresh Unscented Clumping Walnut Cat Litter, 14-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_SWHEAT_MULTI_14LB": {
            "name": "sWheat Scoop Multi-Cat Natural Clumping Wheat Cat Litter, 14-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_BOXIECAT_UNSC_16LB": {
            "name": "Boxiecat Unscented Odor Control Clumping Clay Cat & Kitty Litter, 16-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_BOXIECAT_AIR_PROBIOTIC_16_5LB": {
            "name": "Boxiecat Air Probiotic Lightweight Clumping Cat & Kitty Litter, 16.5-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_BOXIECAT_AIR_EXTRA_16_5LB": {
            "name": "Boxiecat Air Extra Strength Lightweight Clumping Cat & Kitty Litter, 16.5-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_BOXIECAT_AIR_UNSC_16_5LB": {
            "name": "Boxiecat Air Unscented Lightweight Clumping Cat & Kitty Litter, 16.5-lb bag",
            "category": "Cat Litter",
            "price": 39.99
        },
        "CAT_LITTER_BOXIECAT_AIR_GENTLE_16_5LB": {
            "name": "Boxiecat Air Gently Scented Lightweight Clumping Cat & Kitty Litter, 16.5-lb bag",
            "category": "Cat Litter",
            "price": 49.99
        },
        "CAT_LITTER_BOXIECAT_ECO_16_5LB": {
            "name": "Boxiecat Eco Farm-to-Box Premium Ultra Sustainable Clumping Cat & Kitty Litter, 16.5-lb bag",
            "category": "Cat Litter",
            "price": 69.99
        },
        "CAT_LITTER_DRPOL_PINECOBBLE_14LB": {
            "name": "Dr. Pol Pine Cobble Cat Litter, 14-lb bag",
            "category": "Cat Litter",
            "price": 29.99
        },
        "CAT_LITTER_BOX_COVERED": {
            "name": "Covered Cat Litter Box",
            "category": "Accessories",
            "price": 29.99
        },
        "CAT_LITTER_BOX_AUTOMATIC": {
            "name": "Automatic Self-Cleaning Litter Box",
            "category": "Accessories",
            "price": 149.99
        },

        "CAT_TOY_WAND_FEATHER": {
            "name": "Cat Interactive Wand - Feather",
            "category": "Cat Toys",
            "price": 6.99
        },
        "CAT_TOY_LASER_POINTER": {
            "name": "Cat Laser Pointer",
            "category": "Cat Toys",
            "price": 4.99
        },
        "CAT_SCRATCH_POST_SISAL": {
            "name": "Cat Scratching Post (Sisal)",
            "category": "Accessories",
            "price": 15.99
        },
        "CAT_BED_BOLSTER": {
            "name": "Cat Bolster Bed",
            "category": "Accessories",
            "price": 24.99
        },
        "CAT_GROOMING_BRUSH": {
            "name": "Cat Grooming Brush",
            "category": "Accessories",
            "price": 7.99
        },
        "CAT_WATER_FOUNTAIN": {
            "name": "Cat Water Fountain",
            "category": "Accessories",
            "price": 34.99
        },

        "CAT_FLEA_TICK_TOPICAL": {
            "name": "Cat Flea & Tick Topical (OTC)",
            "category": "Cat Health & Wellness",
            "price": 18.99
        },
        "CAT_VITAMIN_HAIRBALL": {
            "name": "Cat Hairball Control Supplement",
            "category": "Cat Health & Wellness",
            "price": 9.99
        },
        "CAT_DENTAL_WATER_ADDITIVE": {
            "name": "Cat Dental Water Additive",
            "category": "Cat Health & Wellness",
            "price": 8.99
        },
        "CAT_EAR_CLEANER": {
            "name": "Cat Ear Cleaner (Antiseptic)",
            "category": "Cat Health & Wellness",
            "price": 6.99
        },

        "RABBIT_FOOD_PELLETS": {
            "name": "Rabbit Food Pellets",
            "category": "Small Pet",
            "price": 8.99
        },
        "GUINEA_PIG_FOOD_VITC": {
            "name": "Guinea Pig Food (with Vitamin C)",
            "category": "Small Pet",
            "price": 10.99
        },
        "TIMOTHY_HAY_BAG": {
            "name": "Timothy Hay (Small Pets) Bag",
            "category": "Small Pet",
            "price": 14.99
        },
        "HAMSTER_BEDDING_PAPER": {
            "name": "Paper-Based Small Pet Bedding",
            "category": "Small Pet",
            "price": 9.99
        },
        "RABBIT_CAGE_LARGE": {
            "name": "Large Rabbit Cage",
            "category": "Accessories",
            "price": 59.99
        },
        "SMALL_PET_WHEEL_PLASTIC": {
            "name": "Hamster Exercise Wheel",
            "category": "Accessories",
            "price": 12.99
        },
        "GUINEA_PIG_HIDEOUT": {
            "name": "Guinea Pig Hideout",
            "category": "Accessories",
            "price": 9.49
        },
        "CHINCHILLA_DUST_BATH": {
            "name": "Chinchilla Dust Bath",
            "category": "Small Pet",
            "price": 7.99
        },

        "REPTILE_PELLET_DIET": {
            "name": "Reptile Pellet Diet",
            "category": "Reptile Food",
            "price": 9.99
        },
        "FROZEN_MICE_PACK": {
            "name": "Frozen Mice (5-pack)",
            "category": "Reptile Food",
            "price": 12.99
        },
        "REPTILE_TERRARIUM_40GAL": {
            "name": "Reptile Terrarium 40 Gallon",
            "category": "Reptile Enclosures",
            "price": 129.99
        },
        "REPTILE_HEAT_LAMP": {
            "name": "Reptile Heat Lamp (UVB)",
            "category": "Reptile Heating & Lighting",
            "price": 24.99
        },
        "REPTILE_BARK_SUBSTRATE": {
            "name": "Reptile Bark Substrate",
            "category": "Reptile Substrate",
            "price": 11.99
        },
        "REPTILE_HUMIDITY_FOGGER": {
            "name": "Reptile Fogger/Humidifier",
            "category": "Reptile Water & Humidity",
            "price": 39.99
        },
        "REPTILE_CALCIUM_SUPPLEMENT": {
            "name": "Reptile Calcium Dust",
            "category": "Reptile Health",
            "price": 5.99
        },

        "AQUARIUM_STARTER_KIT_10GAL": {
            "name": "Aquarium Starter Kit - 10 Gallon",
            "category": "Fish & Aquatic Supplies",
            "price": 59.99
        },
        "AQUARIUM_FILTER_HOB": {
            "name": "Hang-On-Back Aquarium Filter",
            "category": "Fish & Aquatic Supplies",
            "price": 29.99
        },
        "WATER_CONDITIONER_DECHLOR": {
            "name": "Aquarium Water Conditioner (Dechlor)",
            "category": "Fish & Aquatic Supplies",
            "price": 5.99
        },
        "FISH_FOOD_FLAKES": {
            "name": "Fish Food - Flakes",
            "category": "Fish Food",
            "price": 4.99
        },
        "FISH_FOOD_FROZEN_BLOODWORMS": {
            "name": "Frozen Bloodworms (Blister Pack)",
            "category": "Fish Food",
            "price": 8.49
        },
        "AQUARIUM_HEATER_100W": {
            "name": "Aquarium Heater 100W",
            "category": "Fish & Aquatic Equipment",
            "price": 19.99
        },
        "AQUARIUM_GRAVEL_VAC": {
            "name": "Aquarium Gravel Vacuum",
            "category": "Fish & Aquatic Maintenance",
            "price": 12.99
        },

        "BIRD_SEED_PARAKEET": {
            "name": "Bird Seed Blend - Parakeet",
            "category": "Bird Food",
            "price": 8.99
        },
        "BIRD_SEED_PARROT": {
            "name": "Bird Seed Blend - Parrot",
            "category": "Bird Food",
            "price": 14.99
        },
        "BIRD_CAGE_MEDIUM": {
            "name": "Medium Bird Cage",
            "category": "Bird Cages",
            "price": 49.99
        },
        "BIRD_TOY_FORAGING": {
            "name": "Bird Foraging Toy",
            "category": "Bird Toys",
            "price": 8.99
        },
        "CUTTLEBONE_CALCIUM": {
            "name": "Bird Cuttlebone (Calcium)",
            "category": "Bird Health & Grooming",
            "price": 3.99
        },
        "CHICKEN_COOP_SMALL": {
            "name": "Small Chicken Coop",
            "category": "Chicken & Poultry Supplies",
            "price": 199.99
        },
        "LAYER_FEED_25LB": {
            "name": "Layer Feed 25 lbs (Chickens)",
            "category": "Chicken & Poultry Supplies",
            "price": 16.99
        },

        "HORSE_FEED_SENIOR": {
            "name": "Horse Feed (Senior)",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_TREAT_APPLE": {
            "name": "Horse Treat - Apple Crunch",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_GROOMING_BRUSH_SET": {
            "name": "Horse Grooming Brush Set",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_FLY_SPRAY": {
            "name": "Horse Fly Spray",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "GOAT_FEED_20LB": {
            "name": "Goat Feed 20 lbs",
            "category": "Farm Animal Feed",
            "price": 12.99
        },
        "PIG_FEED_25LB": {
            "name": "Pig Feed 25 lbs",
            "category": "Farm Animal Feed",
            "price": 17.99
        },

        "PET_GATE_INDOOR": {
            "name": "Indoor Pet Gate",
            "category": "Gates & Playpens",
            "price": 39.99
        },
        "PET_CLEANING_ODOR_REMOVER": {
            "name": "Pet Stain & Odor Remover",
            "category": "Cleaning & Odor Control",
            "price": 8.99
        },
        "PET_CALMING_DIFFUSER": {
            "name": "Pet Calming Pheromone Diffuser",
            "category": "Training & Behavior",
            "price": 22.99
        },
        "PET_CAMERA_WIFI": {
            "name": "WiFi Pet Camera",
            "category": "Pet Tech",
            "price": 129.99
        },
        "TRAINING_CLICKER": {
            "name": "Training Clicker",
            "category": "Training & Behavior",
            "price": 2.99
        },

        "WILD_BIRD_SEED_10LB": {
            "name": "Wild Bird Seed 10 lbs",
            "category": "Wild Bird Supplies",
            "price": 8.99
        },
        "BEEKEEPING_STARTER_KIT": {
            "name": "Beekeeping Starter Kit",
            "category": "Beekeeping Supplies",
            "price": 79.99
        },

        "PPP_VET_DIET_UR_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets UR St/Ox Urinary Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_UR_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets UR St/Ox Urinary Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_UR_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets UR St/Ox Urinary Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_DM_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_DM_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_DM_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_OM_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_OM_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_OM_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_HA_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_HA_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_HA_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_EN_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Feline Formula Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_EN_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Feline Formula Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_EN_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Feline Formula Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_NF_ADV_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_NF_ADV_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_NF_ADV_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_NF_EARLY_DRY_CAT_FOOD_5LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_NF_EARLY_DRY_CAT_FOOD_9LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Dry Cat Food, 9-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_NF_EARLY_DRY_CAT_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_EN_NAT_DRY_CAT_FOOD_4LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Naturals Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 56.99
        },
        "PPP_VET_DIET_EN_NAT_DRY_CAT_FOOD_8LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Naturals Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 87.99
        },
        "PPP_VET_DIET_EN_NAT_DRY_CAT_FOOD_14LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Naturals Dry Cat Food, 14-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 107.99
        },
        "PPP_VET_DIET_DH_DRY_CAT_FOOD_4LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 56.99
        },
        "PPP_VET_DIET_DH_DRY_CAT_FOOD_8LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 87.99
        },
        "PPP_VET_DIET_DH_DRY_CAT_FOOD_14LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Cat Food, 14-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 107.99
        },
        "PPP_VET_DIET_EN_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Cat Food, 5.5-oz can, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 56.99
        },
        "PPP_VET_DIET_EN_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Cat Food, 5.5-oz can, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 87.99
        },
        "PPP_VET_DIET_EN_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Cat Food, 5.5-oz can, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 107.99
        },
        "PPP_VET_DIET_UR_SS_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary St/Ox Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_UR_SS_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary St/Ox Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_UR_SS_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary St/Ox Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 117.99
        },
        "PPP_VET_DIET_OM_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "PPP_VET_DIET_OM_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_OM_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Savory Selects Variety Pack Wet Cat Food, 5.5-oz, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 137.99
        },
        "PPP_VET_DIET_DM_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Wet Cat Food, 5.5-oz, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "PPP_VET_DIET_DM_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Wet Cat Food, 5.5-oz, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_DM_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets DM Dietetic Management Wet Cat Food, 5.5-oz, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 137.99
        },
        "PPP_VET_DIET_NF_ADV_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Wet Cat Food, 5.5-oz, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 69.99
        },
        "PPP_VET_DIET_NF_ADV_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Wet Cat Food, 5.5-oz, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 107.99
        },
        "PPP_VET_DIET_NF_ADV_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Advanced Care Wet Cat Food, 5.5-oz, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 147.99
        },
        "PPP_VET_DIET_NF_EARLY_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Wet Cat Food, 5.5-oz, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 49.99
        },
        "PPP_VET_DIET_NF_EARLY_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Wet Cat Food, 5.5-oz, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 87.99
        },
        "PPP_VET_DIET_NF_EARLY_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Early Care Wet Cat Food, 5.5-oz, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 127.99
        },
        "PPP_VET_DIET_EN_SS_CAN_CAT_FOOD_6CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Savory Selects in Gravy with Chicken Wet Cat Food, 5.5-oz can, case of 6",
            "category": "Wet Cat Food (Prescription)",
            "price": 49.99
        },
        "PPP_VET_DIET_EN_SS_CAN_CAT_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Savory Selects in Gravy with Chicken Wet Cat Food, 5.5-oz can, case of 12",
            "category": "Wet Cat Food (Prescription)",
            "price": 87.99
        },
        "PPP_VET_DIET_EN_SS_CAN_CAT_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Savory Selects in Gravy with Chicken Wet Cat Food, 5.5-oz can, case of 24",
            "category": "Wet Cat Food (Prescription)",
            "price": 127.99
        },


        "PPP_VET_DIET_HA_CHICKEN_DRY_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 46.99
        },
        "PPP_VET_DIET_HA_CHICKEN_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 77.99
        },
        "PPP_VET_DIET_HA_CHICKEN_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 97.99
        },
        "PPP_VET_DIET_HA_SALMON_DRY_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Salmon Flavor Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 49.99
        },
        "PPP_VET_DIET_HA_SALMON_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Salmon Flavor Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 80.99
        },
        "PPP_VET_DIET_SALMON_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Salmon Flavor Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 100.99
        },
        "PPP_VET_DIET_HA_VEG_DRY_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Vegetarian Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 51.99
        },
        "PPP_VET_DIET_HA_VEG_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Vegetarian Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 82.99
        },
        "PPP_VET_DIET_HA_VEG_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Vegetarian Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 102.99
        },
        "PPP_VET_DIET_EN_DRY_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 51.99
        },
        "PPP_VET_DIET_EN_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 82.99
        },
        "PPP_VET_DIET_EN_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 102.99
        },
        "PPP_VET_DIET_OM_SB_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Select Blend Chicken Flavor Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 51.99
        },
        "PPP_VET_DIET_OM_SB_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Select Blend Chicken Flavor Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 82.99
        },
        "PPP_VET_DIET_OM_SB_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Select Blend Chicken Flavor Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 102.99
        },
        "PPP_VET_DIET_OM_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_OM_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_OM_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_JM_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets JM Joint Mobility Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_JM_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets JM Joint Mobility Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_JM_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets JM Joint Mobility Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_NEURO_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets Neurocare Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_NEURO_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets Neurocare Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_NEURO_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets Neurocare Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_EN_FB_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Fiber Balance Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_EN_FB_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Fiber Balance Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_EN_FB_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Fiber Balance Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_EL_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets El Elemental Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_EL_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets El Elemental Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_EL_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets El Elemental Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_OM_JM_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Metabolic Response Plus Joint Mobility Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_OM_JM_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Metabolic Response Plus Joint Mobility Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_OM_JM_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets OM Metabolic Response Plus Joint Mobility Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_CC_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets CC CardioCare High Protein Chicken Flavor Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_CC_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets CC CardioCare High Protein Chicken Flavor Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_CC_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets CC CardioCare High Protein Chicken Flavor Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_NF_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_NF_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_NF_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_UR_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_UR_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_UR_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_DRM_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets DRM Dermatologic Management Naturals Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_DRM_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets DRM Dermatologic Management Naturals Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_DRM_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets DRM Dermatologic Management Naturals Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_DH_DOG_FOOD_6LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 65.99
        },
        "PPP_VET_DIET_DH_DRY_DOG_FOOD_16LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Dog Food, 16-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "PPP_VET_DIET_DH_DRY_DOG_FOOD_25LB": {
            "name": "Purina Pro Plan Veterinary Diets DH Dental Health Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "PPP_VET_DIET_EN_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Dog Food, 13.4-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_EN_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Dog Food, 13.4-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_EN_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Wet Dog Food, 13.4-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_HA_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Wet Dog Food, 13.3-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_HA_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Wet Dog Food, 13.3-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_HA_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets HA Hydrolyzed Chicken Flavor Wet Dog Food, 13.3-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_OM_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Wet Dog Food, 13.3-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_OM_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Wet Dog Food, 13.3-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_OM_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets OM Overweight Management Wet Dog Food, 13.3-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_UR_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Wet Dog Food, 13.3-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_UR_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Wet Dog Food, 13.3-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_UR_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets UR Urinary Ox/St Wet Dog Food, 13.3-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_NF_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Wet Dog Food, 13.3-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_NF_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Wet Dog Food, 13.3-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_NF_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets NF Kidney Function Wet Dog Food, 13.3-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_CN_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets CN Critical Nutrition Wet Dog & Cat Food, 5.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_CN_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets CN Critical Nutrition Wet Dog & Cat Food, 5.5-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_CN_CAN_DOG_FOOD_48CASE": {
            "name": "Purina Pro Plan Veterinary Diets CN Critical Nutrition Wet Dog & Cat Food, 5.5-oz, case of 48",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_EN_LF_CAN_DOG_FOOD_4CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Low Fat Wet Dog Food, 13.4-oz, case of 4",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_EN_LF_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Low Fat Wet Dog Food, 13.4-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_EN_LF_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Gastroenteric Low Fat Wet Dog Food, 13.4-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },
        "PPP_VET_DIET_EN_VP_CAN_DOG_FOOD_12CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Savory Selects Gastroenteric with Chicken in-Gravy & Lamb Chunks-in-Gravy Variety Pack Wet Adult Dog Food, 13.3-oz can, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 44.99
        },
        "PPP_VET_DIET_EN_VP_CAN_DOG_FOOD_24CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Savory Selects Gastroenteric with Chicken in-Gravy & Lamb Chunks-in-Gravy Variety Pack Wet Adult Dog Food, 13.3-oz can, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "PPP_VET_DIET_EN_VP_CAN_DOG_FOOD_48CASE": {
            "name": "Purina Pro Plan Veterinary Diets EN Savory Selects Gastroenteric with Chicken in-Gravy & Lamb Chunks-in-Gravy Variety Pack Wet Adult Dog Food, 13.3-oz can, case of 48",
            "category": "Wet Dog Food (Prescription)",
            "price": 149.99
        },

        "BB_VET_DIET_HF_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 47.99
        },
        "BB_VET_DIET_HF_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "BB_VET_DIET_KS_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet KS Kidney Support Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 39.99
        },
        "BB_VET_DIET_KS_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet KS Kidney Support Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 104.99
        },
        "BB_VET_DIET_GI_LF_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Low Fat Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 39.99
        },
        "BB_VET_DIET_GI_LF_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Low Fat Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "BB_VET_DIET_WU_UR_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 37.99
        },
        "BB_VET_DIET_WU_UR_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "BB_VET_DIET_NP_AL_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet NP Novel Protein Alligator Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "BB_VET_DIET_NP_AL_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet NP Novel Protein Alligator Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "BB_VET_DIET_GI_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 38.99
        },
        "BB_VET_DIET_GI_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 98.99
        },
        "BB_VET_DIET_WM_MS_DRY_DOG_FOOD_6LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+M Weight Management + Mobility Support Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 43.99
        },
        "BB_VET_DIET_WM_MS_DRY_DOG_FOOD_22LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+M Weight Management + Mobility Support Dry Dog Food, 22-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 109.99
        },
        "BB_VET_DIET_KS_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet KS Kidney Support Grain-Free Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 54.96
        },
        "BB_VET_DIET_KS_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet KS Kidney Support Grain-Free Wet Dog Food, 12.5-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 104.96
        },
        "BB_VET_DIET_HF_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 68.99
        },
        "BB_VET_DIET_HF_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Wet Dog Food, 12.5-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 131.99
        },
        "BB_VET_DIET_GI_LF_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Low Fat Grain-Free Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 69.94
        },
        "BB_VET_DIET_GI_LF_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Low Fat Grain-Free Wet Dog Food, 12.5-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 122.94
        },
        "BB_VET_DIET_WU_UR_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 54.96
        },
        "BB_VET_DIET_WU_UR_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 104.96
        },
        "BB_VET_DIET_WM_MS_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+M Weight Management + Mobility Support Grain-Free Wet Dog Food, 12.5-oz, case of 12",
            "category": "Wet Dog Food (Prescription)",
            "price": 54.96
        },
        "BB_VET_DIET_WM_MS_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+M Weight Management + Mobility Support Grain-Free Wet Dog Food, 12.5-oz, case of 24",
            "category": "Wet Dog Food (Prescription)",
            "price": 104.96
        },
        "BB_VET_DIET_GI_CAN_DOG_FOOD_12CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet Gastrointestinal Support Chicken Wet Dog Food, 12.5-oz can, 12 count",
            "category": "Wet Dog Food (Prescription)",
            "price": 54.96
        },
        "BB_VET_DIET_GI_CAN_DOG_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet Gastrointestinal Support Chicken Wet Dog Food, 12.5-oz can, 24 count",
            "category": "Wet Dog Food (Prescription)",
            "price": 104.96
        },

        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_6.5LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Grain-Free Dry Cat Food, 6.5-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_16LB": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Grain-Free Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_7LB": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_18LB": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Grain-Free Dry Cat Food, 18-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_7LB": {
            "name": "Blue Buffalo Natural Veterinary Diet K+M Kidney + Mobility Support Grain-Free Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_18LB": {
            "name": "Blue Buffalo Natural Veterinary Diet K+M Kidney + Mobility Support Grain-Free Dry Cat Food, 18-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_7LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Grain-Free Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_18LB": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Grain-Free Dry Cat Food, 18-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_7LB": {
            "name": "Blue Buffalo Natural Veterinary Diet NP Novel Protein Alligator Grain-Free Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_DRY_CAT_FOOD_18LB": {
            "name": "Blue Buffalo Natural Veterinary Diet NP Novel Protein Alligator Grain-Free Dry Cat Food, 18-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 94.99
        },


        "BB_VET_DIET_WU_UR_CAN_CAT_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Cat Food, 5.5-oz can, 24 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_CAN_CAT_FOOD_48CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Cat Food, 5.5-oz can, 48 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_WU_UR_CAN_CAT_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Cat Food, 5.5-oz can, 24 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_WU_UR_CAN_CAT_FOOD_48CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet W+U Weight Management + Urinary Care Chicken Wet Cat Food, 5.5-oz can, 48 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_HF_CAN_CAT_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Salmon Wet Cat Food, 5.5-oz can, 24 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_HF_CAN_CAT_FOOD_48CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet HF Hydrolyzed for Food Intolerance Salmon Wet Cat Food, 5.5-oz can, 48 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_GI_CAN_CAT_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Chicken Wet Cat Food, 5.5-oz can, 24 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_GI_CAN_CAT_FOOD_48CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet GI Gastrointestinal Support Chicken Wet Cat Food, 5.5-oz can, 48 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 94.99
        },
        "BB_VET_DIET_KM_MS_CAN_CAT_FOOD_24CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet K+M Kidney + Mobility Support Grain-Free Wet Cat Food, 5.5-oz, 24 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 52.99
        },
        "BB_VET_DIET_KM_MS_CAN_CAT_FOOD_48CASE": {
            "name": "Blue Buffalo Natural Veterinary Diet K+M Kidney + Mobility Support Grain-Free Wet Cat Food, 5.5-oz, 48 count",
            "category": "Wet Cat Food (Prescription)",
            "price": 94.99
        },

        "DOG_RX_HEARTGARD_UPTO25_6": {
            "name": "Heartgard Plus Chew for Dogs, up to 25 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_HEARTGARD_26_50_6": {
            "name": "Heartgard Plus Chew for Dogs, 26-50 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_HEARTGARD_51_100_6": {
            "name": "Heartgard Plus Chew for Dogs, 51-100 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_NEXGARD_4_10_3": {
            "name": "NexGard Chewables for Dogs, 4-10 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_NEXGARD_10_24_3": {
            "name": "NexGard Chewables for Dogs, 10.1-24 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_NEXGARD_24_60_3": {
            "name": "NexGard Chewables for Dogs, 24.1-60 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_NEXGARD_60_121_3": {
            "name": "NexGard Chewables for Dogs, 60.1-121 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_APOQUEL_3_6MG_100": {
            "name": "Apoquel Tablets for Dogs, 3.6 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_APOQUEL_5_4MG_100": {
            "name": "Apoquel Tablets for Dogs, 5.4 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_APOQUEL_16MG_100": {
            "name": "Apoquel Tablets for Dogs, 16 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_GALLIPRANT_20MG_30": {
            "name": "Galliprant Tablets for Dogs, 20 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_GALLIPRANT_60MG_30": {
            "name": "Galliprant Tablets for Dogs, 60 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_GALLIPRANT_100MG_30": {
            "name": "Galliprant Tablets for Dogs, 100 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_SIMPARICATRIO_2_8_5_5_3": {
            "name": "Simparica Trio Chewable for Dogs, 2.8-5.5 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_SIMPARICATRIO_5_6_11_3": {
            "name": "Simparica Trio Chewable for Dogs, 5.6-11 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_SIMPARICATRIO_11_22_3": {
            "name": "Simparica Trio Chewable for Dogs, 11.1-22 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_SIMPARICATRIO_22_44_3": {
            "name": "Simparica Trio Chewable for Dogs, 22.1-44 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_SIMPARICATRIO_44_88_3": {
            "name": "Simparica Trio Chewable for Dogs, 44.1-88 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_SIMPARICATRIO_88_132_3": {
            "name": "Simparica Trio Chewable for Dogs, 88.1-132 lbs (3 Chews)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_CREDELIOQUATTRO_6_12_6": {
            "name": "Credelio Quattro Chewable Tablets for Dogs, 6.1-12 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_CREDELIOQUATTRO_12_25_6": {
            "name": "Credelio Quattro Chewable Tablets for Dogs, 12.1-25 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_CREDELIOQUATTRO_25_50_6": {
            "name": "Credelio Quattro Chewable Tablets for Dogs, 25.1-50 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_CREDELIOQUATTRO_50_100_6": {
            "name": "Credelio Quattro Chewable Tablets for Dogs, 50.1-100 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_TRIFEXIS_10_20_6": {
            "name": "Trifexis Chewable Tablet for Dogs, 10-20 lbs (6 Tablets)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_TRIFEXIS_20_40_6": {
            "name": "Trifexis Chewable Tablet for Dogs, 20.1-40 lbs (6 Tablets)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_TRIFEXIS_40_60_6": {
            "name": "Trifexis Chewable Tablet for Dogs, 40.1-60 lbs (6 Tablets)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_TRIFEXIS_60_120_6": {
            "name": "Trifexis Chewable Tablet for Dogs, 60.1-120 lbs (6 Tablets)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_SENTINELSPECTRUM_8_2_25_4": {
            "name": "Sentinel Spectrum Chews for Dogs, 8.1-25 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_SENTINELSPECTRUM_25_50_6": {
            "name": "Sentinel Spectrum Chews for Dogs, 25.1-50 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_SENTINELSPECTRUM_50_100_6": {
            "name": "Sentinel Spectrum Chews for Dogs, 50.1-100 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_ADVANTAGEMULTI_DOG_9_20": {
            "name": "Advantage Multi Topical Solution for Dogs, 9-20 lbs (1 dose)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_ADVANTAGEMULTI_DOG_20_55": {
            "name": "Advantage Multi Topical Solution for Dogs, 20-55 lbs (1 dose)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_ADVANTAGEMULTI_DOG_55_88": {
            "name": "Advantage Multi Topical Solution for Dogs, 55-88 lbs (1 dose)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "CAT_RX_ADVANTAGEMULTI_CAT_5_9": {
            "name": "Advantage Multi Topical Solution for Cats, 5-9 lbs (1 dose)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "CAT_RX_ADVANTAGEMULTI_CAT_9_18": {
            "name": "Advantage Multi Topical Solution for Cats, 9-18 lbs (1 dose)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_INTERCEPTORPLUS_8_25_6": {
            "name": "Interceptor Plus Chewable for Dogs, 8-25 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_INTERCEPTORPLUS_25_50_6": {
            "name": "Interceptor Plus Chewable for Dogs, 25.1-50 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_INTERCEPTORPLUS_50_100_6": {
            "name": "Interceptor Plus Chewable for Dogs, 50.1-100 lbs (6 Chews)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_CARPROFEN_25MG_60": {
            "name": "Carprofen (Rimadyl) Caplets for Dogs, 25 mg (60 count)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_CARPROFEN_75MG_60": {
            "name": "Carprofen (Rimadyl) Caplets for Dogs, 75 mg (60 count)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_CARPROFEN_100MG_60": {
            "name": "Carprofen (Rimadyl) Caplets for Dogs, 100 mg (60 count)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_VETMEDIN_1_25MG_50": {
            "name": "Vetmedin Chewable Tablets for Dogs, 1.25 mg (50 count)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_VETMEDIN_5MG_50": {
            "name": "Vetmedin Chewable Tablets for Dogs, 5 mg (50 count)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "HORSE_RX_BANAMINE_50MGML_100ML": {
            "name": "Banamine Injectable Solution for Horses & Cattle, 50 mg/mL (100 mL)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "HORSE_RX_PHENYLBUTAZONE_POWDER_2_2LB": {
            "name": "Phenylbutazone Powder for Horses, 2.2 lbs",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_FIROCOXIB_57MG_30": {
            "name": "Previcox (Firocoxib) Chewable Tablets for Dogs, 57 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_FIROCOXIB_227MG_30": {
            "name": "Previcox (Firocoxib) Chewable Tablets for Dogs, 227 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "HORSE_RX_EQUIOXX_57MG_60": {
            "name": "Equioxx Tablets for Horses, 57 mg (60 count)",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "HORSE_RX_EQUIOXX_PASTE_6_93G": {
            "name": "Equioxx Oral Paste for Horses, 6.93 g syringe",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_ADEQUAN_CANINE_5ML": {
            "name": "Adequan Canine (Polysulfated Glycosaminoglycan) Injection, 100 mg/mL, 5 mL",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_AMOXICILLIN_500MG_100": {
            "name": "Amoxicillin Capsules, 500 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 59.99
        },
        "DOG_RX_GABAPENTIN_300MG_100": {
            "name": "Gabapentin Capsules, 300 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 79.99
        },
        "DOG_RX_THYROTABS_0_8MG_120": {
            "name": "Thyro-Tabs Tablets for Dogs, 0.8 mg (120 count)",
            "category": "Pharmacy RX",
            "price": 99.99
        },
        "DOG_RX_SILEO_0_09MGML_3ML": {
            "name": "Sileo (dexmedetomidine) Oromucosal Gel for Dogs, 0.09 mg/mL, 3 mL",
            "category": "Pharmacy RX",
            "price": 129.99
        },
        "DOG_RX_FUROSEMIDE_12_5MG_100": {
            "name": "Furosemide Tablets for Dogs & Cats, 12.5 mg (100 count)",
            "category": "Pharmacy RX",
            "price": 19.99
        },
        "DOG_RX_INCURIN_1MG_30": {
            "name": "Incurin (Estriol) Tablets for Dogs, 1 mg (30 count)",
            "category": "Pharmacy RX",
            "price": 29.99
        },
        "DOG_RX_PROIN_50MG_60": {
            "name": "Proin ER Chewable Tablets for Dogs, 50 mg (60 count)",
            "category": "Pharmacy RX",
            "price": 59.99
        },


        "DOG_COLLAR_FRISCO_BLACK_XS": {
            "name": "Frisco Black Dog Collar, XS",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_COLLAR_FRISCO_BLACK_S": {
            "name": "Frisco Black Dog Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_COLLAR_FRISCO_BLACK_M": {
            "name": "Frisco Black Dog Collar, M",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_COLLAR_FRISCO_BLUE_XS": {
            "name": "Frisco Blue Dog Collar, XS",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_COLLAR_FRISCO_BLUE_S": {
            "name": "Frisco Blue Dog Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_COLLAR_FRISCO_BLUE_M": {
            "name": "Frisco Blue Dog Collar, M",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_COLLAR_FRISCO_PINK_XS": {
            "name": "Frisco Pink Dog Collar, XS",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_COLLAR_FRISCO_PINK_S": {
            "name": "Frisco Pink Dog Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_COLLAR_FRISCO_PINK_M": {
            "name": "Frisco Pink Dog Collar, M",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_COLLAR_FRISCO_RED_XS": {
            "name": "Frisco Red Dog Collar, XS",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_COLLAR_FRISCO_RED_S": {
            "name": "Frisco Red Dog Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_COLLAR_FRISCO_RED_M": {
            "name": "Frisco Red Dog Collar, M",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_COLLAR_BLUEBERRY_REFLECTIVE_BLUE_XS": {
            "name": "Blueberry Reflective Blue Dog Collar, XS",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_COLLAR_BLUEBERRY_REFLECTIVE_BLUE_S": {
            "name": "Blueberry Reflective Blue Dog Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_COLLAR_BLUEBERRY_REFLECTIVE_BLUE_M": {
            "name": "Blueberry Reflective Blue Dog Collar, M",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_COLLAR_BLUEBERRY_FLORAL_GREEN_XS": {
            "name": "Blueberry Floral Green Dog Collar, XS",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_COLLAR_BLUEBERRY_FLORAL_GREEN_S": {
            "name": "Blueberry Floral Green Dog Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_COLLAR_BLUEBERRY_FLORAL_GREEN_M": {
            "name": "Blueberry Floral Green Dog Collar, M",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_COLLAR_BLUEBERRY_STRIPE_PINK_XS": {
            "name": "Blueberry Stripe Pink Dog Collar, XS",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_COLLAR_BLUEBERRY_STRIPE_PINK_S": {
            "name": "Blueberry Stripe Pink Dog Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_COLLAR_BLUEBERRY_STRIPE_PINK_M": {
            "name": "Blueberry Stripe Pink Dog Collar, M",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_COLLAR_LUPINEPET_MOUNTAIN_LAKE_XS": {
            "name": "Lupinepet Mountain Lake Dog Collar, XS",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_COLLAR_LUPINEPET_MOUNTAIN_LAKE_S": {
            "name": "Lupinepet Mountain Lake Dog Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_COLLAR_LUPINEPET_MOUNTAIN_LAKE_M": {
            "name": "Lupinepet Mountain Lake Dog Collar, M",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_COLLAR_LUPINEPET_SEA_GLASS_XS": {
            "name": "Lupinepet Sea Glass Dog Collar, XS",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_COLLAR_LUPINEPET_SEA_GLASS_S": {
            "name": "Lupinepet Sea Glass Dog Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_COLLAR_LUPINEPET_SEA_GLASS_M": {
            "name": "Lupinepet Sea Glass Dog Collar, M",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_COLLAR_LUPINEPET_PURPLE_RAIN_XS": {
            "name": "Lupinepet Purple Rain Dog Collar, XS",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_COLLAR_LUPINEPET_PURPLE_RAIN_S": {
            "name": "Lupinepet Purple Rain Dog Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_COLLAR_LUPINEPET_PURPLE_RAIN_M": {
            "name": "Lupinepet Purple Rain Dog Collar, M",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_BLACK_XS": {
            "name": "Go Tags Custom Engraved Black Dog Collar, XS",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_BLACK_S": {
            "name": "Go Tags Custom Engraved Black Dog Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_BLACK_M": {
            "name": "Go Tags Custom Engraved Black Dog Collar, M",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_RED_XS": {
            "name": "Go Tags Custom Engraved Red Dog Collar, XS",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_RED_S": {
            "name": "Go Tags Custom Engraved Red Dog Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_COLLAR_GO_TAGS_CUSTOM_ENGRAVED_RED_M": {
            "name": "Go Tags Custom Engraved Red Dog Collar, M",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_HOT_PINK_XS": {
            "name": "Red Dingo Classic Hot Pink Dog Collar, XS",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_HOT_PINK_S": {
            "name": "Red Dingo Classic Hot Pink Dog Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_HOT_PINK_M": {
            "name": "Red Dingo Classic Hot Pink Dog Collar, M",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_TURQUOISE_XS": {
            "name": "Red Dingo Classic Turquoise Dog Collar, XS",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_TURQUOISE_S": {
            "name": "Red Dingo Classic Turquoise Dog Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_TURQUOISE_M": {
            "name": "Red Dingo Classic Turquoise Dog Collar, M",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_LIME_XS": {
            "name": "Red Dingo Classic Lime Dog Collar, XS",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_LIME_S": {
            "name": "Red Dingo Classic Lime Dog Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_COLLAR_RED_DINGO_CLASSIC_LIME_M": {
            "name": "Red Dingo Classic Lime Dog Collar, M",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_LEASH_FRISCO_NYLON_BLACK_4FT": {
            "name": "Frisco Nylon Black Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_LEASH_FRISCO_NYLON_BLACK_6FT": {
            "name": "Frisco Nylon Black Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_LEASH_FRISCO_NYLON_BLUE_4FT": {
            "name": "Frisco Nylon Blue Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_LEASH_FRISCO_NYLON_BLUE_6FT": {
            "name": "Frisco Nylon Blue Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_LEASH_FRISCO_NYLON_PINK_4FT": {
            "name": "Frisco Nylon Pink Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_LEASH_FRISCO_NYLON_PINK_6FT": {
            "name": "Frisco Nylon Pink Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_LEASH_COUNTRY_BROOK_PAISLEY_PURPLE_4FT": {
            "name": "Country Brook Paisley Purple Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_LEASH_COUNTRY_BROOK_PAISLEY_PURPLE_6FT": {
            "name": "Country Brook Paisley Purple Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_LEASH_COUNTRY_BROOK_CHEVRON_TEAL_4FT": {
            "name": "Country Brook Chevron Teal Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_LEASH_COUNTRY_BROOK_CHEVRON_TEAL_6FT": {
            "name": "Country Brook Chevron Teal Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_LEASH_HURTTA_ADJUSTABLE_ROPE_RAVEN_4FT": {
            "name": "Hurtta Adjustable Rope Raven Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_LEASH_HURTTA_ADJUSTABLE_ROPE_RAVEN_6FT": {
            "name": "Hurtta Adjustable Rope Raven Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_LEASH_HURTTA_ADJUSTABLE_ROPE_PEACOCK_4FT": {
            "name": "Hurtta Adjustable Rope Peacock Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_LEASH_HURTTA_ADJUSTABLE_ROPE_PEACOCK_6FT": {
            "name": "Hurtta Adjustable Rope Peacock Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_LEASH_HURTTA_WEEKEND_WARRIOR_NEON_LEMON_4FT": {
            "name": "Hurtta Weekend Warrior Neon Lemon Dog Leash, 4-ft",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_LEASH_HURTTA_WEEKEND_WARRIOR_NEON_LEMON_6FT": {
            "name": "Hurtta Weekend Warrior Neon Lemon Dog Leash, 6-ft",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_BLACK_XS": {
            "name": "Frisco Padded Nylon Black Dog Harness, XS",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_BLACK_S": {
            "name": "Frisco Padded Nylon Black Dog Harness, S",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_BLACK_M": {
            "name": "Frisco Padded Nylon Black Dog Harness, M",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_RED_XS": {
            "name": "Frisco Padded Nylon Red Dog Harness, XS",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_RED_S": {
            "name": "Frisco Padded Nylon Red Dog Harness, S",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_HARNESS_FRISCO_PADDED_NYLON_RED_M": {
            "name": "Frisco Padded Nylon Red Dog Harness, M",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLACK_MESH_XS": {
            "name": "Best Pet Supplies Voyager Black Mesh Dog Harness, XS",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLACK_MESH_S": {
            "name": "Best Pet Supplies Voyager Black Mesh Dog Harness, S",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLACK_MESH_M": {
            "name": "Best Pet Supplies Voyager Black Mesh Dog Harness, M",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLUE_MESH_XS": {
            "name": "Best Pet Supplies Voyager Blue Mesh Dog Harness, XS",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLUE_MESH_S": {
            "name": "Best Pet Supplies Voyager Blue Mesh Dog Harness, S",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_BLUE_MESH_M": {
            "name": "Best Pet Supplies Voyager Blue Mesh Dog Harness, M",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_PINK_MESH_XS": {
            "name": "Best Pet Supplies Voyager Pink Mesh Dog Harness, XS",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_PINK_MESH_S": {
            "name": "Best Pet Supplies Voyager Pink Mesh Dog Harness, S",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_HARNESS_BEST_PET_SUPPLIES_VOYAGER_PINK_MESH_M": {
            "name": "Best Pet Supplies Voyager Pink Mesh Dog Harness, M",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_TWILIGHT_GRAY_XS": {
            "name": "Ruffwear Front Range Twilight Gray Dog Harness, XS",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_TWILIGHT_GRAY_S": {
            "name": "Ruffwear Front Range Twilight Gray Dog Harness, S",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_TWILIGHT_GRAY_M": {
            "name": "Ruffwear Front Range Twilight Gray Dog Harness, M",
            "category": "Accessories",
            "price": 22.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_HIBISCUS_PINK_XS": {
            "name": "Ruffwear Front Range Hibiscus Pink Dog Harness, XS",
            "category": "Accessories",
            "price": 24.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_HIBISCUS_PINK_S": {
            "name": "Ruffwear Front Range Hibiscus Pink Dog Harness, S",
            "category": "Accessories",
            "price": 29.99
        },
        "DOG_HARNESS_RUFFWEAR_FRONT_RANGE_HIBISCUS_PINK_M": {
            "name": "Ruffwear Front Range Hibiscus Pink Dog Harness, M",
            "category": "Accessories",
            "price": 8.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_COWBOYS_XS": {
            "name": "Pets First NFL Cowboys Dog Harness, XS",
            "category": "Accessories",
            "price": 9.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_COWBOYS_S": {
            "name": "Pets First NFL Cowboys Dog Harness, S",
            "category": "Accessories",
            "price": 12.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_COWBOYS_M": {
            "name": "Pets First NFL Cowboys Dog Harness, M",
            "category": "Accessories",
            "price": 14.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_PATRIOTS_XS": {
            "name": "Pets First NFL Patriots Dog Harness, XS",
            "category": "Accessories",
            "price": 17.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_PATRIOTS_S": {
            "name": "Pets First NFL Patriots Dog Harness, S",
            "category": "Accessories",
            "price": 19.99
        },
        "DOG_HARNESS_PETS_FIRST_NFL_PATRIOTS_M": {
            "name": "Pets First NFL Patriots Dog Harness, M",
            "category": "Accessories",
            "price": 22.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S88": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S89": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 29.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S90": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 8.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S91": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 9.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S92": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 12.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S93": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 14.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S94": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 17.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S95": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 19.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S96": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 22.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S97": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 24.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S98": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 29.99
        },
        "CAT_COLLAR_TRAVEL_CAT_ADVENTURE_BLACK_S99": {
            "name": "Travel Cat Adventure Black Cat Collar, S",
            "category": "Accessories",
            "price": 8.99
        },

        "DOG_SHAMPOO_ANDIS_PUPPY_GENTLE": {
            "name": "Andis Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_SHAMPOO_ANDIS_ODOR_CONTROL": {
            "name": "Andis Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_SHAMPOO_ANDIS_WHITENING": {
            "name": "Andis Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_SHAMPOO_ANDIS_OATMEAL": {
            "name": "Andis Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_BRUSH_ANDIS_SLICKER_SMALL": {
            "name": "Andis Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_BRUSH_ANDIS_PIN_MEDIUM": {
            "name": "Andis Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_BRUSH_ANDIS_DESHEDDING_LARGE": {
            "name": "Andis Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_CLIPPER_ANDIS_CORDLESS": {
            "name": "Andis Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_CLIPPER_ANDIS_2-SPEED": {
            "name": "Andis 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_CLIPPER_ANDIS_5-IN-1": {
            "name": "Andis 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_NAIL_GRINDER_ANDIS_RECHARGEABLE": {
            "name": "Andis Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_NAIL_GRINDER_ANDIS_2-SPEED": {
            "name": "Andis 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_EAR_CLEANER_ANDIS_ALOE": {
            "name": "Andis Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_EAR_CLEANER_ANDIS_MEDICATED": {
            "name": "Andis Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_TOOTHPASTE_ANDIS_MINT": {
            "name": "Andis Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_TOOTHPASTE_ANDIS_PEANUT_BUTTER": {
            "name": "Andis Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_SHAMPOO_WAHL_PUPPY_GENTLE": {
            "name": "Wahl Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_SHAMPOO_WAHL_ODOR_CONTROL": {
            "name": "Wahl Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_SHAMPOO_WAHL_WHITENING": {
            "name": "Wahl Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_SHAMPOO_WAHL_OATMEAL": {
            "name": "Wahl Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_BRUSH_WAHL_SLICKER_SMALL": {
            "name": "Wahl Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_BRUSH_WAHL_PIN_MEDIUM": {
            "name": "Wahl Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_BRUSH_WAHL_DESHEDDING_LARGE": {
            "name": "Wahl Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_CLIPPER_WAHL_CORDLESS": {
            "name": "Wahl Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_CLIPPER_WAHL_2-SPEED": {
            "name": "Wahl 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_CLIPPER_WAHL_5-IN-1": {
            "name": "Wahl 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_NAIL_GRINDER_WAHL_RECHARGEABLE": {
            "name": "Wahl Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_NAIL_GRINDER_WAHL_2-SPEED": {
            "name": "Wahl 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_EAR_CLEANER_WAHL_ALOE": {
            "name": "Wahl Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_EAR_CLEANER_WAHL_MEDICATED": {
            "name": "Wahl Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_TOOTHPASTE_WAHL_MINT": {
            "name": "Wahl Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_TOOTHPASTE_WAHL_PEANUT_BUTTER": {
            "name": "Wahl Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_SHAMPOO_OSTER_PUPPY_GENTLE": {
            "name": "Oster Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_SHAMPOO_OSTER_ODOR_CONTROL": {
            "name": "Oster Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_SHAMPOO_OSTER_WHITENING": {
            "name": "Oster Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_SHAMPOO_OSTER_OATMEAL": {
            "name": "Oster Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_BRUSH_OSTER_SLICKER_SMALL": {
            "name": "Oster Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_BRUSH_OSTER_PIN_MEDIUM": {
            "name": "Oster Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_BRUSH_OSTER_DESHEDDING_LARGE": {
            "name": "Oster Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_CLIPPER_OSTER_CORDLESS": {
            "name": "Oster Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_CLIPPER_OSTER_2-SPEED": {
            "name": "Oster 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_CLIPPER_OSTER_5-IN-1": {
            "name": "Oster 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_NAIL_GRINDER_OSTER_RECHARGEABLE": {
            "name": "Oster Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_NAIL_GRINDER_OSTER_2-SPEED": {
            "name": "Oster 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_EAR_CLEANER_OSTER_ALOE": {
            "name": "Oster Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_EAR_CLEANER_OSTER_MEDICATED": {
            "name": "Oster Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_TOOTHPASTE_OSTER_MINT": {
            "name": "Oster Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_TOOTHPASTE_OSTER_PEANUT_BUTTER": {
            "name": "Oster Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_SHAMPOO_FURMINATOR_PUPPY_GENTLE": {
            "name": "FURminator Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_SHAMPOO_FURMINATOR_ODOR_CONTROL": {
            "name": "FURminator Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_SHAMPOO_FURMINATOR_WHITENING": {
            "name": "FURminator Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_SHAMPOO_FURMINATOR_OATMEAL": {
            "name": "FURminator Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_BRUSH_FURMINATOR_SLICKER_SMALL": {
            "name": "FURminator Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_BRUSH_FURMINATOR_PIN_MEDIUM": {
            "name": "FURminator Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_BRUSH_FURMINATOR_DESHEDDING_LARGE": {
            "name": "FURminator Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_CLIPPER_FURMINATOR_CORDLESS": {
            "name": "FURminator Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_CLIPPER_FURMINATOR_2-SPEED": {
            "name": "FURminator 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_CLIPPER_FURMINATOR_5-IN-1": {
            "name": "FURminator 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_NAIL_GRINDER_FURMINATOR_RECHARGEABLE": {
            "name": "FURminator Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_NAIL_GRINDER_FURMINATOR_2-SPEED": {
            "name": "FURminator 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_EAR_CLEANER_FURMINATOR_ALOE": {
            "name": "FURminator Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_EAR_CLEANER_FURMINATOR_MEDICATED": {
            "name": "FURminator Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_TOOTHPASTE_FURMINATOR_MINT": {
            "name": "FURminator Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_TOOTHPASTE_FURMINATOR_PEANUT_BUTTER": {
            "name": "FURminator Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_SHAMPOO_FRISCO_PUPPY_GENTLE": {
            "name": "Frisco Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_SHAMPOO_FRISCO_ODOR_CONTROL": {
            "name": "Frisco Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_SHAMPOO_FRISCO_WHITENING": {
            "name": "Frisco Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_SHAMPOO_FRISCO_OATMEAL": {
            "name": "Frisco Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_BRUSH_FRISCO_SLICKER_SMALL": {
            "name": "Frisco Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_BRUSH_FRISCO_PIN_MEDIUM": {
            "name": "Frisco Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_BRUSH_FRISCO_DESHEDDING_LARGE": {
            "name": "Frisco Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_CLIPPER_FRISCO_CORDLESS": {
            "name": "Frisco Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_CLIPPER_FRISCO_2-SPEED": {
            "name": "Frisco 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_CLIPPER_FRISCO_5-IN-1": {
            "name": "Frisco 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_NAIL_GRINDER_FRISCO_RECHARGEABLE": {
            "name": "Frisco Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_NAIL_GRINDER_FRISCO_2-SPEED": {
            "name": "Frisco 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_EAR_CLEANER_FRISCO_ALOE": {
            "name": "Frisco Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_EAR_CLEANER_FRISCO_MEDICATED": {
            "name": "Frisco Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_TOOTHPASTE_FRISCO_MINT": {
            "name": "Frisco Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_TOOTHPASTE_FRISCO_PEANUT_BUTTER": {
            "name": "Frisco Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_SHAMPOO_BIO-GROOM_PUPPY_GENTLE": {
            "name": "Bio-Groom Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_SHAMPOO_BIO-GROOM_ODOR_CONTROL": {
            "name": "Bio-Groom Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_SHAMPOO_BIO-GROOM_WHITENING": {
            "name": "Bio-Groom Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_SHAMPOO_BIO-GROOM_OATMEAL": {
            "name": "Bio-Groom Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_BRUSH_BIO-GROOM_SLICKER_SMALL": {
            "name": "Bio-Groom Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_BRUSH_BIO-GROOM_PIN_MEDIUM": {
            "name": "Bio-Groom Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_BRUSH_BIO-GROOM_DESHEDDING_LARGE": {
            "name": "Bio-Groom Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_CLIPPER_BIO-GROOM_CORDLESS": {
            "name": "Bio-Groom Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_CLIPPER_BIO-GROOM_2-SPEED": {
            "name": "Bio-Groom 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_CLIPPER_BIO-GROOM_5-IN-1": {
            "name": "Bio-Groom 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_NAIL_GRINDER_BIO-GROOM_RECHARGEABLE": {
            "name": "Bio-Groom Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_NAIL_GRINDER_BIO-GROOM_2-SPEED": {
            "name": "Bio-Groom 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_EAR_CLEANER_BIO-GROOM_ALOE": {
            "name": "Bio-Groom Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_EAR_CLEANER_BIO-GROOM_MEDICATED": {
            "name": "Bio-Groom Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_TOOTHPASTE_BIO-GROOM_MINT": {
            "name": "Bio-Groom Mint Toothpaste for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_TOOTHPASTE_BIO-GROOM_PEANUT_BUTTER": {
            "name": "Bio-Groom Peanut Butter Toothpaste for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_SHAMPOO_HARTZ_PUPPY_GENTLE": {
            "name": "Hartz Puppy Gentle Shampoo for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_SHAMPOO_HARTZ_ODOR_CONTROL": {
            "name": "Hartz Odor Control Shampoo for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_SHAMPOO_HARTZ_WHITENING": {
            "name": "Hartz Whitening Shampoo for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_SHAMPOO_HARTZ_OATMEAL": {
            "name": "Hartz Oatmeal Shampoo for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_BRUSH_HARTZ_SLICKER_SMALL": {
            "name": "Hartz Slicker Small Brush for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "DOG_BRUSH_HARTZ_PIN_MEDIUM": {
            "name": "Hartz Pin Medium Brush for Dogs",
            "category": "Grooming",
            "price": 12.99
        },
        "DOG_BRUSH_HARTZ_DESHEDDING_LARGE": {
            "name": "Hartz Deshedding Large Brush for Dogs",
            "category": "Grooming",
            "price": 14.99
        },
        "DOG_CLIPPER_HARTZ_CORDLESS": {
            "name": "Hartz Cordless Clipper for Dogs",
            "category": "Grooming",
            "price": 17.99
        },
        "DOG_CLIPPER_HARTZ_2-SPEED": {
            "name": "Hartz 2-Speed Clipper for Dogs",
            "category": "Grooming",
            "price": 19.99
        },
        "DOG_CLIPPER_HARTZ_5-IN-1": {
            "name": "Hartz 5-in-1 Clipper for Dogs",
            "category": "Grooming",
            "price": 22.99
        },
        "DOG_NAIL_GRINDER_HARTZ_RECHARGEABLE": {
            "name": "Hartz Rechargeable Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 24.99
        },
        "DOG_NAIL_GRINDER_HARTZ_2-SPEED": {
            "name": "Hartz 2-Speed Nail Grinder for Dogs",
            "category": "Grooming",
            "price": 29.99
        },
        "DOG_EAR_CLEANER_HARTZ_ALOE": {
            "name": "Hartz Aloe Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 8.99
        },
        "DOG_EAR_CLEANER_HARTZ_MEDICATED": {
            "name": "Hartz Medicated Ear Cleaner for Dogs",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_SHAMPOO_FURMINATOR_HYPOALLERGENIC": {
            "name": "FURminator Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_SHAMPOO_FURMINATOR_WATERLESS": {
            "name": "FURminator Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_SHAMPOO_FURMINATOR_DEODORIZING": {
            "name": "FURminator Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_BRUSH_FURMINATOR_SOFT_SLICKER": {
            "name": "FURminator Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_BRUSH_FURMINATOR_DESHEDDING": {
            "name": "FURminator Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_BRUSH_FURMINATOR_FLEA_COMB": {
            "name": "FURminator Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_NAIL_CLIPPER_FURMINATOR_SCISSOR": {
            "name": "FURminator Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_NAIL_CLIPPER_FURMINATOR_GUILLOTINE": {
            "name": "FURminator Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_FUR_ROLLER_FURMINATOR_LINT_REMOVER": {
            "name": "FURminator Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_FUR_ROLLER_FURMINATOR_SELF-CLEANING": {
            "name": "FURminator Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_EAR_CLEANER_FURMINATOR_GENTLE": {
            "name": "FURminator Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_EAR_CLEANER_FURMINATOR_MEDICATED": {
            "name": "FURminator Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_TOOTHPASTE_FURMINATOR_TUNA": {
            "name": "FURminator Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_TOOTHPASTE_FURMINATOR_CHICKEN": {
            "name": "FURminator Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_SHAMPOO_HARTZ_HYPOALLERGENIC": {
            "name": "Hartz Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_SHAMPOO_HARTZ_WATERLESS": {
            "name": "Hartz Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_SHAMPOO_HARTZ_DEODORIZING": {
            "name": "Hartz Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_BRUSH_HARTZ_SOFT_SLICKER": {
            "name": "Hartz Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_BRUSH_HARTZ_DESHEDDING": {
            "name": "Hartz Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_BRUSH_HARTZ_FLEA_COMB": {
            "name": "Hartz Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_NAIL_CLIPPER_HARTZ_SCISSOR": {
            "name": "Hartz Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_NAIL_CLIPPER_HARTZ_GUILLOTINE": {
            "name": "Hartz Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_FUR_ROLLER_HARTZ_LINT_REMOVER": {
            "name": "Hartz Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_FUR_ROLLER_HARTZ_SELF-CLEANING": {
            "name": "Hartz Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_EAR_CLEANER_HARTZ_GENTLE": {
            "name": "Hartz Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_EAR_CLEANER_HARTZ_MEDICATED": {
            "name": "Hartz Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_TOOTHPASTE_HARTZ_TUNA": {
            "name": "Hartz Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_TOOTHPASTE_HARTZ_CHICKEN": {
            "name": "Hartz Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_SHAMPOO_TROPICLEAN_HYPOALLERGENIC": {
            "name": "TropiClean Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_SHAMPOO_TROPICLEAN_WATERLESS": {
            "name": "TropiClean Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_SHAMPOO_TROPICLEAN_DEODORIZING": {
            "name": "TropiClean Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_BRUSH_TROPICLEAN_SOFT_SLICKER": {
            "name": "TropiClean Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_BRUSH_TROPICLEAN_DESHEDDING": {
            "name": "TropiClean Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_BRUSH_TROPICLEAN_FLEA_COMB": {
            "name": "TropiClean Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_NAIL_CLIPPER_TROPICLEAN_SCISSOR": {
            "name": "TropiClean Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_NAIL_CLIPPER_TROPICLEAN_GUILLOTINE": {
            "name": "TropiClean Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_FUR_ROLLER_TROPICLEAN_LINT_REMOVER": {
            "name": "TropiClean Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_FUR_ROLLER_TROPICLEAN_SELF-CLEANING": {
            "name": "TropiClean Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_EAR_CLEANER_TROPICLEAN_GENTLE": {
            "name": "TropiClean Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_EAR_CLEANER_TROPICLEAN_MEDICATED": {
            "name": "TropiClean Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_TOOTHPASTE_TROPICLEAN_TUNA": {
            "name": "TropiClean Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_TOOTHPASTE_TROPICLEAN_CHICKEN": {
            "name": "TropiClean Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_SHAMPOO_EARTHBATH_HYPOALLERGENIC": {
            "name": "Earthbath Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_SHAMPOO_EARTHBATH_WATERLESS": {
            "name": "Earthbath Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_SHAMPOO_EARTHBATH_DEODORIZING": {
            "name": "Earthbath Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_BRUSH_EARTHBATH_SOFT_SLICKER": {
            "name": "Earthbath Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_BRUSH_EARTHBATH_DESHEDDING": {
            "name": "Earthbath Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_BRUSH_EARTHBATH_FLEA_COMB": {
            "name": "Earthbath Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_NAIL_CLIPPER_EARTHBATH_SCISSOR": {
            "name": "Earthbath Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_NAIL_CLIPPER_EARTHBATH_GUILLOTINE": {
            "name": "Earthbath Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_FUR_ROLLER_EARTHBATH_LINT_REMOVER": {
            "name": "Earthbath Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_FUR_ROLLER_EARTHBATH_SELF-CLEANING": {
            "name": "Earthbath Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_EAR_CLEANER_EARTHBATH_GENTLE": {
            "name": "Earthbath Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_EAR_CLEANER_EARTHBATH_MEDICATED": {
            "name": "Earthbath Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_TOOTHPASTE_EARTHBATH_TUNA": {
            "name": "Earthbath Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_TOOTHPASTE_EARTHBATH_CHICKEN": {
            "name": "Earthbath Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_SHAMPOO_CHOMCHOMROLLER_HYPOALLERGENIC": {
            "name": "ChomChom Roller Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_SHAMPOO_CHOMCHOMROLLER_WATERLESS": {
            "name": "ChomChom Roller Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_SHAMPOO_CHOMCHOMROLLER_DEODORIZING": {
            "name": "ChomChom Roller Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_BRUSH_CHOMCHOMROLLER_SOFT_SLICKER": {
            "name": "ChomChom Roller Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_BRUSH_CHOMCHOMROLLER_DESHEDDING": {
            "name": "ChomChom Roller Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_BRUSH_CHOMCHOMROLLER_FLEA_COMB": {
            "name": "ChomChom Roller Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_NAIL_CLIPPER_CHOMCHOMROLLER_SCISSOR": {
            "name": "ChomChom Roller Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_NAIL_CLIPPER_CHOMCHOMROLLER_GUILLOTINE": {
            "name": "ChomChom Roller Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_FUR_ROLLER_CHOMCHOMROLLER_LINT_REMOVER": {
            "name": "ChomChom Roller Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_FUR_ROLLER_CHOMCHOMROLLER_SELF-CLEANING": {
            "name": "ChomChom Roller Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_EAR_CLEANER_CHOMCHOMROLLER_GENTLE": {
            "name": "ChomChom Roller Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_EAR_CLEANER_CHOMCHOMROLLER_MEDICATED": {
            "name": "ChomChom Roller Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_TOOTHPASTE_CHOMCHOMROLLER_TUNA": {
            "name": "ChomChom Roller Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_TOOTHPASTE_CHOMCHOMROLLER_CHICKEN": {
            "name": "ChomChom Roller Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_SHAMPOO_NECOICHI_HYPOALLERGENIC": {
            "name": "Necoichi Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_SHAMPOO_NECOICHI_WATERLESS": {
            "name": "Necoichi Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_SHAMPOO_NECOICHI_DEODORIZING": {
            "name": "Necoichi Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_BRUSH_NECOICHI_SOFT_SLICKER": {
            "name": "Necoichi Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_BRUSH_NECOICHI_DESHEDDING": {
            "name": "Necoichi Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_BRUSH_NECOICHI_FLEA_COMB": {
            "name": "Necoichi Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_NAIL_CLIPPER_NECOICHI_SCISSOR": {
            "name": "Necoichi Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_NAIL_CLIPPER_NECOICHI_GUILLOTINE": {
            "name": "Necoichi Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_FUR_ROLLER_NECOICHI_LINT_REMOVER": {
            "name": "Necoichi Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_FUR_ROLLER_NECOICHI_SELF-CLEANING": {
            "name": "Necoichi Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_EAR_CLEANER_NECOICHI_GENTLE": {
            "name": "Necoichi Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_EAR_CLEANER_NECOICHI_MEDICATED": {
            "name": "Necoichi Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_TOOTHPASTE_NECOICHI_TUNA": {
            "name": "Necoichi Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_TOOTHPASTE_NECOICHI_CHICKEN": {
            "name": "Necoichi Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_SHAMPOO_PURRDYPAWS_HYPOALLERGENIC": {
            "name": "Purrdy Paws Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_SHAMPOO_PURRDYPAWS_WATERLESS": {
            "name": "Purrdy Paws Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_SHAMPOO_PURRDYPAWS_DEODORIZING": {
            "name": "Purrdy Paws Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_BRUSH_PURRDYPAWS_SOFT_SLICKER": {
            "name": "Purrdy Paws Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_BRUSH_PURRDYPAWS_DESHEDDING": {
            "name": "Purrdy Paws Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_BRUSH_PURRDYPAWS_FLEA_COMB": {
            "name": "Purrdy Paws Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_NAIL_CLIPPER_PURRDYPAWS_SCISSOR": {
            "name": "Purrdy Paws Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_NAIL_CLIPPER_PURRDYPAWS_GUILLOTINE": {
            "name": "Purrdy Paws Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_FUR_ROLLER_PURRDYPAWS_LINT_REMOVER": {
            "name": "Purrdy Paws Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_FUR_ROLLER_PURRDYPAWS_SELF-CLEANING": {
            "name": "Purrdy Paws Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_EAR_CLEANER_PURRDYPAWS_GENTLE": {
            "name": "Purrdy Paws Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_EAR_CLEANER_PURRDYPAWS_MEDICATED": {
            "name": "Purrdy Paws Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_TOOTHPASTE_PURRDYPAWS_TUNA": {
            "name": "Purrdy Paws Tuna Toothpaste for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_TOOTHPASTE_PURRDYPAWS_CHICKEN": {
            "name": "Purrdy Paws Chicken Toothpaste for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_SHAMPOO_SAFARI_HYPOALLERGENIC": {
            "name": "Safari Hypoallergenic Shampoo for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_SHAMPOO_SAFARI_WATERLESS": {
            "name": "Safari Waterless Shampoo for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_SHAMPOO_SAFARI_DEODORIZING": {
            "name": "Safari Deodorizing Shampoo for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CAT_BRUSH_SAFARI_SOFT_SLICKER": {
            "name": "Safari Soft Slicker Brush for Cats",
            "category": "Grooming",
            "price": 24.99
        },
        "CAT_BRUSH_SAFARI_DESHEDDING": {
            "name": "Safari Deshedding Brush for Cats",
            "category": "Grooming",
            "price": 29.99
        },
        "CAT_BRUSH_SAFARI_FLEA_COMB": {
            "name": "Safari Flea Comb Brush for Cats",
            "category": "Grooming",
            "price": 8.99
        },
        "CAT_NAIL_CLIPPER_SAFARI_SCISSOR": {
            "name": "Safari Scissor Nail Clipper for Cats",
            "category": "Grooming",
            "price": 9.99
        },
        "CAT_NAIL_CLIPPER_SAFARI_GUILLOTINE": {
            "name": "Safari Guillotine Nail Clipper for Cats",
            "category": "Grooming",
            "price": 12.99
        },
        "CAT_FUR_ROLLER_SAFARI_LINT_REMOVER": {
            "name": "Safari Lint Remover Fur Roller for Cats",
            "category": "Grooming",
            "price": 14.99
        },
        "CAT_FUR_ROLLER_SAFARI_SELF-CLEANING": {
            "name": "Safari Self-Cleaning Fur Roller for Cats",
            "category": "Grooming",
            "price": 17.99
        },
        "CAT_EAR_CLEANER_SAFARI_GENTLE": {
            "name": "Safari Gentle Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 19.99
        },
        "CAT_EAR_CLEANER_SAFARI_MEDICATED": {
            "name": "Safari Medicated Ear Cleaner for Cats",
            "category": "Grooming",
            "price": 22.99
        },
        "CLEAN_FRISCO_PEE_PAD_XS": {
            "name": "Frisco XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_FRISCO_PEE_PAD_S": {
            "name": "Frisco S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_FRISCO_PEE_PAD_M": {
            "name": "Frisco M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_FRISCO_PEE_PAD_L": {
            "name": "Frisco L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_FRISCO_PEE_PAD_XL": {
            "name": "Frisco XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_FRISCO_DOG_DIAPER_XS": {
            "name": "Frisco XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_FRISCO_DOG_DIAPER_S": {
            "name": "Frisco S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_FRISCO_DOG_DIAPER_M": {
            "name": "Frisco M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_FRISCO_DOG_DIAPER_L": {
            "name": "Frisco L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_FRISCO_DOG_DIAPER_XL": {
            "name": "Frisco XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_FRISCO_FEMALE_WRAP_XS": {
            "name": "Frisco XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_FRISCO_FEMALE_WRAP_S": {
            "name": "Frisco S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_FRISCO_FEMALE_WRAP_M": {
            "name": "Frisco M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_FRISCO_FEMALE_WRAP_L": {
            "name": "Frisco L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_FRISCO_MALE_WRAP_XS": {
            "name": "Frisco XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_FRISCO_MALE_WRAP_S": {
            "name": "Frisco S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_FRISCO_MALE_WRAP_M": {
            "name": "Frisco M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_FRISCO_MALE_WRAP_L": {
            "name": "Frisco L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_FRISCO_PAD_HOLDER_Medium": {
            "name": "Frisco Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_FRISCO_PAD_HOLDER_Large": {
            "name": "Frisco Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_FRISCO_TURF_Standard": {
            "name": "Frisco Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_FRISCO_TURF_Large": {
            "name": "Frisco Large 24x34 Turf",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_WEE-WEE_PEE_PAD_XS": {
            "name": "Wee-Wee XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_WEE-WEE_PEE_PAD_S": {
            "name": "Wee-Wee S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_WEE-WEE_PEE_PAD_M": {
            "name": "Wee-Wee M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_WEE-WEE_PEE_PAD_L": {
            "name": "Wee-Wee L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_WEE-WEE_PEE_PAD_XL": {
            "name": "Wee-Wee XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_WEE-WEE_DOG_DIAPER_XS": {
            "name": "Wee-Wee XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_WEE-WEE_DOG_DIAPER_S": {
            "name": "Wee-Wee S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_WEE-WEE_DOG_DIAPER_M": {
            "name": "Wee-Wee M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_WEE-WEE_DOG_DIAPER_L": {
            "name": "Wee-Wee L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_WEE-WEE_DOG_DIAPER_XL": {
            "name": "Wee-Wee XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_WEE-WEE_FEMALE_WRAP_XS": {
            "name": "Wee-Wee XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_WEE-WEE_FEMALE_WRAP_S": {
            "name": "Wee-Wee S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_WEE-WEE_FEMALE_WRAP_M": {
            "name": "Wee-Wee M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_WEE-WEE_FEMALE_WRAP_L": {
            "name": "Wee-Wee L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_WEE-WEE_MALE_WRAP_XS": {
            "name": "Wee-Wee XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_WEE-WEE_MALE_WRAP_S": {
            "name": "Wee-Wee S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_WEE-WEE_MALE_WRAP_M": {
            "name": "Wee-Wee M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_WEE-WEE_MALE_WRAP_L": {
            "name": "Wee-Wee L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_WEE-WEE_PAD_HOLDER_Medium": {
            "name": "Wee-Wee Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_WEE-WEE_PAD_HOLDER_Large": {
            "name": "Wee-Wee Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_WEE-WEE_TURF_Standard": {
            "name": "Wee-Wee Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_WEE-WEE_TURF_Large": {
            "name": "Wee-Wee Large 24x34 Turf",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_SIMPLESOLUTION_PEE_PAD_XS": {
            "name": "Simple Solution XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_SIMPLESOLUTION_PEE_PAD_S": {
            "name": "Simple Solution S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_SIMPLESOLUTION_PEE_PAD_M": {
            "name": "Simple Solution M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_SIMPLESOLUTION_PEE_PAD_L": {
            "name": "Simple Solution L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_SIMPLESOLUTION_PEE_PAD_XL": {
            "name": "Simple Solution XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_SIMPLESOLUTION_DOG_DIAPER_XS": {
            "name": "Simple Solution XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_SIMPLESOLUTION_DOG_DIAPER_S": {
            "name": "Simple Solution S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_SIMPLESOLUTION_DOG_DIAPER_M": {
            "name": "Simple Solution M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_SIMPLESOLUTION_DOG_DIAPER_L": {
            "name": "Simple Solution L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_SIMPLESOLUTION_DOG_DIAPER_XL": {
            "name": "Simple Solution XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_SIMPLESOLUTION_FEMALE_WRAP_XS": {
            "name": "Simple Solution XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_SIMPLESOLUTION_FEMALE_WRAP_S": {
            "name": "Simple Solution S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_SIMPLESOLUTION_FEMALE_WRAP_M": {
            "name": "Simple Solution M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_SIMPLESOLUTION_FEMALE_WRAP_L": {
            "name": "Simple Solution L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_SIMPLESOLUTION_MALE_WRAP_XS": {
            "name": "Simple Solution XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_SIMPLESOLUTION_MALE_WRAP_S": {
            "name": "Simple Solution S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_SIMPLESOLUTION_MALE_WRAP_M": {
            "name": "Simple Solution M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_SIMPLESOLUTION_MALE_WRAP_L": {
            "name": "Simple Solution L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_SIMPLESOLUTION_PAD_HOLDER_Medium": {
            "name": "Simple Solution Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_SIMPLESOLUTION_PAD_HOLDER_Large": {
            "name": "Simple Solution Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_SIMPLESOLUTION_TURF_Standard": {
            "name": "Simple Solution Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_SIMPLESOLUTION_TURF_Large": {
            "name": "Simple Solution Large 24x34 Turf",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_PAWINSPIRED_PEE_PAD_XS": {
            "name": "Paw Inspired XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_PAWINSPIRED_PEE_PAD_S": {
            "name": "Paw Inspired S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PAWINSPIRED_PEE_PAD_M": {
            "name": "Paw Inspired M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PAWINSPIRED_PEE_PAD_L": {
            "name": "Paw Inspired L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_PAWINSPIRED_PEE_PAD_XL": {
            "name": "Paw Inspired XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_PAWINSPIRED_DOG_DIAPER_XS": {
            "name": "Paw Inspired XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_PAWINSPIRED_DOG_DIAPER_S": {
            "name": "Paw Inspired S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_PAWINSPIRED_DOG_DIAPER_M": {
            "name": "Paw Inspired M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_PAWINSPIRED_DOG_DIAPER_L": {
            "name": "Paw Inspired L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_PAWINSPIRED_DOG_DIAPER_XL": {
            "name": "Paw Inspired XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_PAWINSPIRED_FEMALE_WRAP_XS": {
            "name": "Paw Inspired XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PAWINSPIRED_FEMALE_WRAP_S": {
            "name": "Paw Inspired S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PAWINSPIRED_FEMALE_WRAP_M": {
            "name": "Paw Inspired M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_PAWINSPIRED_FEMALE_WRAP_L": {
            "name": "Paw Inspired L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_PAWINSPIRED_MALE_WRAP_XS": {
            "name": "Paw Inspired XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_PAWINSPIRED_MALE_WRAP_S": {
            "name": "Paw Inspired S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_PAWINSPIRED_MALE_WRAP_M": {
            "name": "Paw Inspired M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_PAWINSPIRED_MALE_WRAP_L": {
            "name": "Paw Inspired L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_PAWINSPIRED_PAD_HOLDER_Medium": {
            "name": "Paw Inspired Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_PAWINSPIRED_PAD_HOLDER_Large": {
            "name": "Paw Inspired Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PAWINSPIRED_TURF_Standard": {
            "name": "Paw Inspired Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PAWINSPIRED_TURF_Large": {
            "name": "Paw Inspired Large 24x34 Turf",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_HARTZ_PEE_PAD_XS": {
            "name": "Hartz XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_HARTZ_PEE_PAD_S": {
            "name": "Hartz S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_HARTZ_PEE_PAD_M": {
            "name": "Hartz M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_HARTZ_PEE_PAD_L": {
            "name": "Hartz L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_HARTZ_PEE_PAD_XL": {
            "name": "Hartz XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_HARTZ_DOG_DIAPER_XS": {
            "name": "Hartz XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_HARTZ_DOG_DIAPER_S": {
            "name": "Hartz S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_HARTZ_DOG_DIAPER_M": {
            "name": "Hartz M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_HARTZ_DOG_DIAPER_L": {
            "name": "Hartz L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_HARTZ_DOG_DIAPER_XL": {
            "name": "Hartz XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_HARTZ_FEMALE_WRAP_XS": {
            "name": "Hartz XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_HARTZ_FEMALE_WRAP_S": {
            "name": "Hartz S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_HARTZ_FEMALE_WRAP_M": {
            "name": "Hartz M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_HARTZ_FEMALE_WRAP_L": {
            "name": "Hartz L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_HARTZ_MALE_WRAP_XS": {
            "name": "Hartz XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_HARTZ_MALE_WRAP_S": {
            "name": "Hartz S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_HARTZ_MALE_WRAP_M": {
            "name": "Hartz M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_HARTZ_MALE_WRAP_L": {
            "name": "Hartz L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_HARTZ_PAD_HOLDER_Medium": {
            "name": "Hartz Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_HARTZ_PAD_HOLDER_Large": {
            "name": "Hartz Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_HARTZ_TURF_Standard": {
            "name": "Hartz Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_HARTZ_TURF_Large": {
            "name": "Hartz Large 24x34 Turf",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_AMERICANKENNELCLUB_PEE_PAD_XS": {
            "name": "American Kennel Club XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_AMERICANKENNELCLUB_PEE_PAD_S": {
            "name": "American Kennel Club S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_AMERICANKENNELCLUB_PEE_PAD_M": {
            "name": "American Kennel Club M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_AMERICANKENNELCLUB_PEE_PAD_L": {
            "name": "American Kennel Club L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_AMERICANKENNELCLUB_PEE_PAD_XL": {
            "name": "American Kennel Club XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_AMERICANKENNELCLUB_DOG_DIAPER_XS": {
            "name": "American Kennel Club XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_AMERICANKENNELCLUB_DOG_DIAPER_S": {
            "name": "American Kennel Club S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_AMERICANKENNELCLUB_DOG_DIAPER_M": {
            "name": "American Kennel Club M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_AMERICANKENNELCLUB_DOG_DIAPER_L": {
            "name": "American Kennel Club L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_AMERICANKENNELCLUB_DOG_DIAPER_XL": {
            "name": "American Kennel Club XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_AMERICANKENNELCLUB_FEMALE_WRAP_XS": {
            "name": "American Kennel Club XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_AMERICANKENNELCLUB_FEMALE_WRAP_S": {
            "name": "American Kennel Club S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_AMERICANKENNELCLUB_FEMALE_WRAP_M": {
            "name": "American Kennel Club M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_AMERICANKENNELCLUB_FEMALE_WRAP_L": {
            "name": "American Kennel Club L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_AMERICANKENNELCLUB_MALE_WRAP_XS": {
            "name": "American Kennel Club XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_AMERICANKENNELCLUB_MALE_WRAP_S": {
            "name": "American Kennel Club S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_AMERICANKENNELCLUB_MALE_WRAP_M": {
            "name": "American Kennel Club M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_AMERICANKENNELCLUB_MALE_WRAP_L": {
            "name": "American Kennel Club L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_AMERICANKENNELCLUB_PAD_HOLDER_Medium": {
            "name": "American Kennel Club Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_AMERICANKENNELCLUB_PAD_HOLDER_Large": {
            "name": "American Kennel Club Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_AMERICANKENNELCLUB_TURF_Standard": {
            "name": "American Kennel Club Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_AMERICANKENNELCLUB_TURF_Large": {
            "name": "American Kennel Club Large 24x34 Turf",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_GLADFORPETS_PEE_PAD_XS": {
            "name": "Glad for Pets XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_GLADFORPETS_PEE_PAD_S": {
            "name": "Glad for Pets S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_GLADFORPETS_PEE_PAD_M": {
            "name": "Glad for Pets M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_GLADFORPETS_PEE_PAD_L": {
            "name": "Glad for Pets L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_GLADFORPETS_PEE_PAD_XL": {
            "name": "Glad for Pets XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_GLADFORPETS_DOG_DIAPER_XS": {
            "name": "Glad for Pets XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_GLADFORPETS_DOG_DIAPER_S": {
            "name": "Glad for Pets S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_GLADFORPETS_DOG_DIAPER_M": {
            "name": "Glad for Pets M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_GLADFORPETS_DOG_DIAPER_L": {
            "name": "Glad for Pets L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_GLADFORPETS_DOG_DIAPER_XL": {
            "name": "Glad for Pets XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_GLADFORPETS_FEMALE_WRAP_XS": {
            "name": "Glad for Pets XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_GLADFORPETS_FEMALE_WRAP_S": {
            "name": "Glad for Pets S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_GLADFORPETS_FEMALE_WRAP_M": {
            "name": "Glad for Pets M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_GLADFORPETS_FEMALE_WRAP_L": {
            "name": "Glad for Pets L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_GLADFORPETS_MALE_WRAP_XS": {
            "name": "Glad for Pets XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_GLADFORPETS_MALE_WRAP_S": {
            "name": "Glad for Pets S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_GLADFORPETS_MALE_WRAP_M": {
            "name": "Glad for Pets M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_GLADFORPETS_MALE_WRAP_L": {
            "name": "Glad for Pets L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_GLADFORPETS_PAD_HOLDER_Medium": {
            "name": "Glad for Pets Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_GLADFORPETS_PAD_HOLDER_Large": {
            "name": "Glad for Pets Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_GLADFORPETS_TURF_Standard": {
            "name": "Glad for Pets Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_GLADFORPETS_TURF_Large": {
            "name": "Glad for Pets Large 24x34 Turf",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_OUT!_PEE_PAD_XS": {
            "name": "OUT! XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_OUT!_PEE_PAD_S": {
            "name": "OUT! S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_OUT!_PEE_PAD_M": {
            "name": "OUT! M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_OUT!_PEE_PAD_L": {
            "name": "OUT! L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_OUT!_PEE_PAD_XL": {
            "name": "OUT! XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_OUT!_DOG_DIAPER_XS": {
            "name": "OUT! XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_OUT!_DOG_DIAPER_S": {
            "name": "OUT! S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_OUT!_DOG_DIAPER_M": {
            "name": "OUT! M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_OUT!_DOG_DIAPER_L": {
            "name": "OUT! L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_OUT!_DOG_DIAPER_XL": {
            "name": "OUT! XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_OUT!_FEMALE_WRAP_XS": {
            "name": "OUT! XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_OUT!_FEMALE_WRAP_S": {
            "name": "OUT! S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_OUT!_FEMALE_WRAP_M": {
            "name": "OUT! M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_OUT!_FEMALE_WRAP_L": {
            "name": "OUT! L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_OUT!_MALE_WRAP_XS": {
            "name": "OUT! XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_OUT!_MALE_WRAP_S": {
            "name": "OUT! S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_OUT!_MALE_WRAP_M": {
            "name": "OUT! M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_OUT!_MALE_WRAP_L": {
            "name": "OUT! L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_OUT!_PAD_HOLDER_Medium": {
            "name": "OUT! Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_OUT!_PAD_HOLDER_Large": {
            "name": "OUT! Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_OUT!_TURF_Standard": {
            "name": "OUT! Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_OUT!_TURF_Large": {
            "name": "OUT! Large 24x34 Turf",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PETPARENTS_PEE_PAD_XS": {
            "name": "Pet Parents XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PETPARENTS_PEE_PAD_S": {
            "name": "Pet Parents S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_PETPARENTS_PEE_PAD_M": {
            "name": "Pet Parents M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_PETPARENTS_PEE_PAD_L": {
            "name": "Pet Parents L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_PETPARENTS_PEE_PAD_XL": {
            "name": "Pet Parents XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_PETPARENTS_DOG_DIAPER_XS": {
            "name": "Pet Parents XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_PETPARENTS_DOG_DIAPER_S": {
            "name": "Pet Parents S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_PETPARENTS_DOG_DIAPER_M": {
            "name": "Pet Parents M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_PETPARENTS_DOG_DIAPER_L": {
            "name": "Pet Parents L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PETPARENTS_DOG_DIAPER_XL": {
            "name": "Pet Parents XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PETPARENTS_FEMALE_WRAP_XS": {
            "name": "Pet Parents XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_PETPARENTS_FEMALE_WRAP_S": {
            "name": "Pet Parents S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_PETPARENTS_FEMALE_WRAP_M": {
            "name": "Pet Parents M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_PETPARENTS_FEMALE_WRAP_L": {
            "name": "Pet Parents L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_PETPARENTS_MALE_WRAP_XS": {
            "name": "Pet Parents XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_PETPARENTS_MALE_WRAP_S": {
            "name": "Pet Parents S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_PETPARENTS_MALE_WRAP_M": {
            "name": "Pet Parents M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_PETPARENTS_MALE_WRAP_L": {
            "name": "Pet Parents L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_PETPARENTS_PAD_HOLDER_Medium": {
            "name": "Pet Parents Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_PETPARENTS_PAD_HOLDER_Large": {
            "name": "Pet Parents Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_PETPARENTS_TURF_Standard": {
            "name": "Pet Parents Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_PETPARENTS_TURF_Large": {
            "name": "Pet Parents Large 24x34 Turf",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_ROCKET&REX_PEE_PAD_XS": {
            "name": "Rocket & Rex XS 17x24 30-ct Pee Pad",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_ROCKET&REX_PEE_PAD_S": {
            "name": "Rocket & Rex S 22x22 50-ct Pee Pad",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_ROCKET&REX_PEE_PAD_M": {
            "name": "Rocket & Rex M 24x24 100-ct Pee Pad",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_ROCKET&REX_PEE_PAD_L": {
            "name": "Rocket & Rex L 24x36 40-ct Pee Pad",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_ROCKET&REX_PEE_PAD_XL": {
            "name": "Rocket & Rex XL 28x34 60-ct Pee Pad",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_ROCKET&REX_DOG_DIAPER_XS": {
            "name": "Rocket & Rex XS 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_ROCKET&REX_DOG_DIAPER_S": {
            "name": "Rocket & Rex S 20-ct Dog Diaper",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_ROCKET&REX_DOG_DIAPER_M": {
            "name": "Rocket & Rex M 30-ct Dog Diaper",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_ROCKET&REX_DOG_DIAPER_L": {
            "name": "Rocket & Rex L 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_ROCKET&REX_DOG_DIAPER_XL": {
            "name": "Rocket & Rex XL 12-ct Dog Diaper",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_ROCKET&REX_FEMALE_WRAP_XS": {
            "name": "Rocket & Rex XS 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_ROCKET&REX_FEMALE_WRAP_S": {
            "name": "Rocket & Rex S 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_ROCKET&REX_FEMALE_WRAP_M": {
            "name": "Rocket & Rex M 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 14.99
        },
        "CLEAN_ROCKET&REX_FEMALE_WRAP_L": {
            "name": "Rocket & Rex L 12-ct Female Wrap",
            "category": "Cleaning",
            "price": 17.99
        },
        "CLEAN_ROCKET&REX_MALE_WRAP_XS": {
            "name": "Rocket & Rex XS 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 19.99
        },
        "CLEAN_ROCKET&REX_MALE_WRAP_S": {
            "name": "Rocket & Rex S 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 22.99
        },
        "CLEAN_ROCKET&REX_MALE_WRAP_M": {
            "name": "Rocket & Rex M 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 24.99
        },
        "CLEAN_ROCKET&REX_MALE_WRAP_L": {
            "name": "Rocket & Rex L 12-ct Male Wrap",
            "category": "Cleaning",
            "price": 29.99
        },
        "CLEAN_ROCKET&REX_PAD_HOLDER_Medium": {
            "name": "Rocket & Rex Medium 24x24 Pad Holder",
            "category": "Cleaning",
            "price": 8.99
        },
        "CLEAN_ROCKET&REX_PAD_HOLDER_Large": {
            "name": "Rocket & Rex Large 24x36 Pad Holder",
            "category": "Cleaning",
            "price": 9.99
        },
        "CLEAN_ROCKET&REX_TURF_Standard": {
            "name": "Rocket & Rex Standard 20x30 Turf",
            "category": "Cleaning",
            "price": 12.99
        },
        "CLEAN_ROCKET&REX_TURF_Large": {
            "name": "Rocket & Rex Large 24x34 Turf",
            "category": "Cleaning",
            "price": 14.99
        },

        "HORSE_BuckeyeNutrition_Safe_1": {
            "name": "Buckeye Nutrition Safe N Easy 50-lb",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "HORSE_BuckeyeNutrition_Grow_2": {
            "name": "Buckeye Nutrition Grow N Win 40-lb",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_BuckeyeNutrition_Senior_3": {
            "name": "Buckeye Nutrition Senior Balance 50-lb",
            "category": "Horse & Farm",
            "price": 12.99
        },
        "HORSE_Tribute_Kalm_4": {
            "name": "Tribute Kalm N EZ 50-lb",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "HORSE_Tribute_Essential_5": {
            "name": "Tribute Essential K 50-lb",
            "category": "Horse & Farm",
            "price": 17.99
        },
        "HORSE_Tribute_Senior_6": {
            "name": "Tribute Senior Sport 50-lb",
            "category": "Horse & Farm",
            "price": 19.99
        },
        "HORSE_Standlee_Alfalfa_7": {
            "name": "Standlee Alfalfa Pellets 50-lb",
            "category": "Horse & Farm",
            "price": 22.99
        },
        "HORSE_Standlee_Timothy_8": {
            "name": "Standlee Timothy Pellets 40-lb",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_MannaPro_Pelleted_9": {
            "name": "Manna Pro Pelleted Feed 50-lb",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_MannaPro_Cracked_10": {
            "name": "Manna Pro Cracked Corn 40-lb",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "HORSE_BluebonnetFeeds_Intensify_11": {
            "name": "Bluebonnet Feeds Intensify Omega 50-lb",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_BluebonnetFeeds_Ration_12": {
            "name": "Bluebonnet Feeds Ration Balancer 40-lb",
            "category": "Horse & Farm",
            "price": 12.99
        },
        "HORSE_Kent_Equine_13": {
            "name": "Kent Equine Plus 50-lb",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "HORSE_Kent_Pro_14": {
            "name": "Kent Pro Sweet 50-lb",
            "category": "Horse & Farm",
            "price": 17.99
        },
        "HORSE_Nutrena_SafeChoice_15": {
            "name": "Nutrena SafeChoice Original 50-lb",
            "category": "Horse & Farm",
            "price": 19.99
        },
        "HORSE_Nutrena_ProForce_16": {
            "name": "Nutrena ProForce Fuel 50-lb",
            "category": "Horse & Farm",
            "price": 22.99
        },
        "HORSE_StudMuffins_Original_17": {
            "name": "Stud Muffins Original 45-oz",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_StudMuffins_Peppermint_18": {
            "name": "Stud Muffins Peppermint 45-oz",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_Mrs.Pastures_Cookies_19": {
            "name": "Mrs. Pastures Cookies 35-oz",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "HORSE_Mrs.Pastures_Cookies_20": {
            "name": "Mrs. Pastures Cookies 80-oz",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_AtoZHorseCookies_Carrot_21": {
            "name": "A to Z Horse Cookies Carrot 2-lb",
            "category": "Horse & Farm",
            "price": 12.99
        },
        "HORSE_AtoZHorseCookies_Apple_22": {
            "name": "A to Z Horse Cookies Apple 2-lb",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "HORSE_BuckeyeNutrition_Peppermint_23": {
            "name": "Buckeye Nutrition Peppermint 4-lb",
            "category": "Horse & Farm",
            "price": 17.99
        },
        "HORSE_BuckeyeNutrition_Banana_24": {
            "name": "Buckeye Nutrition Banana 4-lb",
            "category": "Horse & Farm",
            "price": 19.99
        },
        "HORSE_MannaPro_Apple_25": {
            "name": "Manna Pro Apple Nuggets 4-lb",
            "category": "Horse & Farm",
            "price": 22.99
        },
        "HORSE_MannaPro_Carrot_26": {
            "name": "Manna Pro Carrot Nuggets 4-lb",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_Kelcies_Pumpkin_27": {
            "name": "Kelcie's Pumpkin Spice 3-lb",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_AniMed_Remission_28": {
            "name": "AniMed Remission 5-lb",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "HORSE_AniMed_Pure_29": {
            "name": "AniMed Pure MSM 2-lb",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_AniMed_Vitamin_30": {
            "name": "AniMed Vitamin E 4-lb",
            "category": "Horse & Farm",
            "price": 12.99
        },
        "HORSE_Farnam_Electro_31": {
            "name": "Farnam Electro Dex 5-lb",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "HORSE_Farnam_Sand_32": {
            "name": "Farnam Sand Clear 10-lb",
            "category": "Horse & Farm",
            "price": 17.99
        },
        "HORSE_Farnam_Joint_33": {
            "name": "Farnam Joint Combo 32-oz",
            "category": "Horse & Farm",
            "price": 19.99
        },
        "HORSE_FinishLine_Fluid_34": {
            "name": "Finish Line Fluid Action 32-oz",
            "category": "Horse & Farm",
            "price": 22.99
        },
        "HORSE_FinishLine_Apple_35": {
            "name": "Finish Line Apple Electrolyte 5-lb",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_FinishLine_Stretch_36": {
            "name": "Finish Line Stretch Run 15-lb",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_Uckele_Tri_37": {
            "name": "Uckele Tri Amino 4-lb",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "HORSE_Uckele_GUT_38": {
            "name": "Uckele GUT 10-lb",
            "category": "Horse & Farm",
            "price": 9.99
        },
        "HORSE_Uckele_Joint_39": {
            "name": "Uckele Joint 6-lb",
            "category": "Horse & Farm",
            "price": 12.99
        },
        "HORSE_Cavalor_Gastro_40": {
            "name": "Cavalor Gastro Aid 4-lb",
            "category": "Horse & Farm",
            "price": 14.99
        },
        "HORSE_Cavalor_Hoof_41": {
            "name": "Cavalor Hoof Aid 5-lb",
            "category": "Horse & Farm",
            "price": 17.99
        },
        "HORSE_Cavalor_Muscle_42": {
            "name": "Cavalor Muscle Force 4-lb",
            "category": "Horse & Farm",
            "price": 19.99
        },
        "HORSE_Equithrive_Joint_43": {
            "name": "Equithrive Joint 2-lb",
            "category": "Horse & Farm",
            "price": 22.99
        },
        "HORSE_Equithrive_Metabolic_44": {
            "name": "Equithrive Metabolic 5-lb",
            "category": "Horse & Farm",
            "price": 24.99
        },
        "HORSE_SmartEquine_SmartFlex_45": {
            "name": "SmartEquine SmartFlex Senior 4-lb",
            "category": "Horse & Farm",
            "price": 29.99
        },
        "HORSE_SmartEquine_SmartHoof_46": {
            "name": "SmartEquine SmartHoof 5-lb",
            "category": "Horse & Farm",
            "price": 8.99
        },
        "DOG_DRY_FARMINA_VL_URINARY_ST_CONTROL_66lb": {
            "name": "Farmina Vet Life Urinary ST/Control Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_URINARY_ST_CONTROL_66lb": {
            "name": "Farmina Vet Life Urinary ST/Control Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_URINARY_ST_CONTROL_22lb": {
            "name": "Farmina Vet Life Urinary ST/Control Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_URINARY_ST_CONTROL_22lb": {
            "name": "Farmina Vet Life Urinary ST/Control Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_URINARY_ST_CONTROL_134OZcan": {
            "name": "Farmina Vet Life Urinary ST/Control Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_URINARY_ST_CONTROL_134OZcan": {
            "name": "Farmina Vet Life Urinary ST/Control Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_URINARY_ST_MANAGEMENT_66lb": {
            "name": "Farmina Vet Life Urinary ST Management Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_URINARY_ST_MANAGEMENT_66lb": {
            "name": "Farmina Vet Life Urinary ST Management Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_URINARY_ST_MANAGEMENT_22lb": {
            "name": "Farmina Vet Life Urinary ST Management Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_URINARY_ST_MANAGEMENT_22lb": {
            "name": "Farmina Vet Life Urinary ST Management Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_URINARY_ST_MANAGEMENT_134OZcan": {
            "name": "Farmina Vet Life Urinary ST Management Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_URINARY_ST_MANAGEMENT_134OZcan": {
            "name": "Farmina Vet Life Urinary ST Management Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_RENAL_66lb": {
            "name": "Farmina Vet Life Renal Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_RENAL_66lb": {
            "name": "Farmina Vet Life Renal Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_RENAL_22lb": {
            "name": "Farmina Vet Life Renal Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_RENAL_22lb": {
            "name": "Farmina Vet Life Renal Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_RENAL_134OZcan": {
            "name": "Farmina Vet Life Renal Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_RENAL_134OZcan": {
            "name": "Farmina Vet Life Renal Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_HYDROLYZED_PROTEIN_66lb": {
            "name": "Farmina Vet Life Hydrolyzed Protein Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_HYDROLYZED_PROTEIN_66lb": {
            "name": "Farmina Vet Life Hydrolyzed Protein Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_HYDROLYZED_PROTEIN_22lb": {
            "name": "Farmina Vet Life Hydrolyzed Protein Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_HYDROLYZED_PROTEIN_22lb": {
            "name": "Farmina Vet Life Hydrolyzed Protein Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_HYDROLYZED_PROTEIN_134OZcan": {
            "name": "Farmina Vet Life Hydrolyzed Protein Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_HYDROLYZED_PROTEIN_134OZcan": {
            "name": "Farmina Vet Life Hydrolyzed Protein Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_GASTROINTESTINAL_66lb": {
            "name": "Farmina Vet Life Gastrointestinal Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_GASTROINTESTINAL_66lb": {
            "name": "Farmina Vet Life Gastrointestinal Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_GASTROINTESTINAL_22lb": {
            "name": "Farmina Vet Life Gastrointestinal Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_GASTROINTESTINAL_22lb": {
            "name": "Farmina Vet Life Gastrointestinal Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_GASTROINTESTINAL_134OZcan": {
            "name": "Farmina Vet Life Gastrointestinal Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_GASTROINTESTINAL_134OZcan": {
            "name": "Farmina Vet Life Gastrointestinal Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_RECOUP_66lb": {
            "name": "Farmina Vet Life Recoup Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_RECOUP_66lb": {
            "name": "Farmina Vet Life Recoup Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_RECOUP_22lb": {
            "name": "Farmina Vet Life Recoup Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_RECOUP_22lb": {
            "name": "Farmina Vet Life Recoup Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_RECOUP_134OZcan": {
            "name": "Farmina Vet Life Recoup Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_RECOUP_134OZcan": {
            "name": "Farmina Vet Life Recoup Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_VL_CALORIE_CONTROL_66lb": {
            "name": "Farmina Vet Life Calorie Control Dry Dog Food, 6.6-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "CAT_DRY_FARMINA_VL_CALORIE_CONTROL_66lb": {
            "name": "Farmina Vet Life Calorie Control Dry Cat Food, 6.6-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_FARMINA_VL_CALORIE_CONTROL_22lb": {
            "name": "Farmina Vet Life Calorie Control Dry Dog Food, 22-lb",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_FARMINA_VL_CALORIE_CONTROL_22lb": {
            "name": "Farmina Vet Life Calorie Control Dry Cat Food, 22-lb",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_CAN_FARMINA_VL_CALORIE_CONTROL_134OZcan": {
            "name": "Farmina Vet Life Calorie Control Wet Dog Food, 13.4-oz can",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_FARMINA_VL_CALORIE_CONTROL_134OZcan": {
            "name": "Farmina Vet Life Calorie Control Wet Cat Food, 13.4-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_FARMINA_ND_LAMB_4_4LB": {
            "name": "Farmina N&D Tropical Selection Lamb Adult Medium & Maxi Dry Dog Food, 4.4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "CAT_CAN_TIKI_VET_GI_HEALTH_2_8OZ": {
            "name": "Tiki Cat Veterinary Solutions GI-Health Wet Cat Food, 2.8-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_TIKI_VET_PH_BALANCE_2_8OZ": {
            "name": "Tiki Cat Veterinary Solutions pH-Balance Urinary Care Wet Cat Food, 2.8-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 129.99
        },
        "CAT_CAN_TIKI_VET_LO_CALORIE_2_8OZ": {
            "name": "Tiki Cat Veterinary Solutions Lo-Calorie Weight Management Wet Cat Food, 2.8-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 59.99
        },
        "CAT_CAN_TIKI_VET_GLUCO_BALANCE_2_8OZ": {
            "name": "Tiki Cat Veterinary Solutions Gluco-Balance Wet Cat Food, 2.8-oz can",
            "category": "Wet Cat Food (Prescription)",
            "price": 99.99
        },
        "CAT_CAN_TIKI_MOUSSE_CHICKEN_2_8OZ": {
            "name": "Tiki Cat Mousse Chicken Recipe Wet Cat Food, 2.8-oz pouch",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 129.99
        },
        "CAT_CAN_TIKI_MOUSSE_TUNA_2_8OZ": {
            "name": "Tiki Cat Mousse Tuna Recipe Wet Cat Food, 2.8-oz pouch",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 59.99
        },
        "CAT_CAN_TIKI_MOUSSE_SALMON_2_8OZ": {
            "name": "Tiki Cat Mousse Salmon Recipe Wet Cat Food, 2.8-oz pouch",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 99.99
        },
        "DOG_DRY_DIAMOND_CARE_SENSITIVITY_25LB": {
            "name": "Diamond CARE Sensitivity Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "DOG_DRY_DIAMOND_CARE_WEIGHT_MANAGEMENT_25LB": {
            "name": "Diamond CARE Weight Management Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_DIAMOND_CARE_URINARY_SUPPORT_25LB": {
            "name": "Diamond CARE Urinary Support Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_DRY_DIAMOND_CARE_GASTROINTESTINAL_25LB": {
            "name": "Diamond CARE Gastrointestinal Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_DRY_DIAMOND_CARE_URINARY_15LB": {
            "name": "Diamond CARE Urinary Support Formula Dry Cat Food, 15-lb bag",
            "category": "Dry Cat Food (Prescription)",
            "price": 59.99
        },
        "DOG_DRY_DIAMOND_MAINTENANCE": {
            "name": "Diamond Maintenance Adult Dry Dog Food, 40-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 99.99
        },
        "DOG_DRY_DIAMOND_NATURALS_CHICKEN_RICE": {
            "name": "Diamond Naturals Chicken & Rice Formula Dry Dog Food, 40-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 129.99
        },
        "DOG_DRY_DIAMOND_NATURALS_LAMB_RICE": {
            "name": "Diamond Naturals Lamb & Rice Formula Dry Dog Food, 40-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "DOG_DRY_DIAMOND_PREMIUM": {
            "name": "Diamond Premium Adult Formula Dry Dog Food, 50-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 99.99
        },
        "DOG_FROZEN_JFFD_CHICKEN_RICE_18OZ": {
            "name": "JustFoodForDogs Chicken & White Rice Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 129.99
        },
        "DOG_FROZEN_JFFD_BEEF_POTATO_18OZ": {
            "name": "JustFoodForDogs Beef & Russet Potato Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "DOG_FROZEN_JFFD_FISH_SWEETPOT_18OZ": {
            "name": "JustFoodForDogs Fish & Sweet Potato Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 99.99
        },
        "DOG_FROZEN_JFFD_TURKEY_MAC_18OZ": {
            "name": "JustFoodForDogs Turkey & Whole Wheat Macaroni Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 129.99
        },
        "DOG_FROZEN_JFFD_LAMB_BROWN_RICE_18OZ": {
            "name": "JustFoodForDogs Lamb & Brown Rice Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 59.99
        },
        "DOG_FROZEN_JFFD_RX_RENAL_SUPPORT_18OZ": {
            "name": "JustFoodForDogs Veterinary Support Renal Support Low Protein Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Prescription)",
            "price": 99.99
        },
        "DOG_FROZEN_JFFD_RX_BALANCED_REMEDY_18OZ": {
            "name": "JustFoodForDogs Veterinary Support Balanced Remedy Frozen Dog Food, 18-oz container",
            "category": "Wet Dog Food (Prescription)",
            "price": 129.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_CHICKEN_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Chicken Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_CHICKEN_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Chicken Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TENDER_BEEF_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Tender Beef Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TENDER_BEEF_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Tender Beef Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TURKEY_GIBLETS_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Turkey & Giblets Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TURKEY_GIBLETS_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Turkey & Giblets Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_LIVER_CHICKEN_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Liver & Chicken Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_LIVER_CHICKEN_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Liver & Chicken Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_SALMON_SHRIMP_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Salmon & Shrimp Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_SALMON_SHRIMP_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Salmon & Shrimp Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_OCEAN_WHITEFISH_TUNA_FEAST_3_OZ": {
            "name": "Fancy Feast Classic Pate Ocean Whitefish & Tuna Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_OCEAN_WHITEFISH_TUNA_FEAST_5_5_OZ": {
            "name": "Fancy Feast Classic Pate Ocean Whitefish & Tuna Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_CHICKEN_FEAST_IN_GRAVY_3_OZ": {
            "name": "Fancy Feast Grilled Chicken Feast in Gravy Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_CHICKEN_FEAST_IN_GRAVY_5_5_OZ": {
            "name": "Fancy Feast Grilled Chicken Feast in Gravy Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SALMON_FEAST_IN_GRAVY_3_OZ": {
            "name": "Fancy Feast Grilled Salmon Feast in Gravy Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SALMON_FEAST_IN_GRAVY_5_5_OZ": {
            "name": "Fancy Feast Grilled Salmon Feast in Gravy Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_TUNA_FEAST_IN_GRAVY_3_OZ": {
            "name": "Fancy Feast Grilled Tuna Feast in Gravy Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_TUNA_FEAST_IN_GRAVY_5_5_OZ": {
            "name": "Fancy Feast Grilled Tuna Feast in Gravy Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SEAFOOD_FEAST_VARIETY_3_OZ": {
            "name": "Fancy Feast Grilled Seafood Feast Variety Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SEAFOOD_FEAST_VARIETY_5_5_OZ": {
            "name": "Fancy Feast Grilled Seafood Feast Variety Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_CHICKEN_FEAST_3_OZ": {
            "name": "Fancy Feast Gravy Lovers Chicken Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_CHICKEN_FEAST_5_5_OZ": {
            "name": "Fancy Feast Gravy Lovers Chicken Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_TURKEY_FEAST_3_OZ": {
            "name": "Fancy Feast Gravy Lovers Turkey Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_TURKEY_FEAST_5_5_OZ": {
            "name": "Fancy Feast Gravy Lovers Turkey Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_FLAKED_TUNA_FEAST_3_OZ": {
            "name": "Fancy Feast Flaked Tuna Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_FLAKED_TUNA_FEAST_5_5_OZ": {
            "name": "Fancy Feast Flaked Tuna Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_PRIMAVERA_CHICKEN_3_OZ": {
            "name": "Fancy Feast Medleys Primavera Chicken Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_PRIMAVERA_CHICKEN_5_5_OZ": {
            "name": "Fancy Feast Medleys Primavera Chicken Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_TUSCANY_SALMON_3_OZ": {
            "name": "Fancy Feast Medleys Tuscany Salmon Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_TUSCANY_SALMON_5_5_OZ": {
            "name": "Fancy Feast Medleys Tuscany Salmon Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_FLORENTINE_TUNA_3_OZ": {
            "name": "Fancy Feast Medleys Florentine Tuna Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_FLORENTINE_TUNA_5_5_OZ": {
            "name": "Fancy Feast Medleys Florentine Tuna Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_CHICKEN_FEAST_3_OZ": {
            "name": "Fancy Feast Creamy Delights Chicken Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_CHICKEN_FEAST_5_5_OZ": {
            "name": "Fancy Feast Creamy Delights Chicken Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_SALMON_FEAST_3_OZ": {
            "name": "Fancy Feast Creamy Delights Salmon Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_SALMON_FEAST_5_5_OZ": {
            "name": "Fancy Feast Creamy Delights Salmon Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_BEEF_FEAST_3_OZ": {
            "name": "Fancy Feast Sliced Beef Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_BEEF_FEAST_5_5_OZ": {
            "name": "Fancy Feast Sliced Beef Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_TURKEY_FEAST_3_OZ": {
            "name": "Fancy Feast Sliced Turkey Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_TURKEY_FEAST_5_5_OZ": {
            "name": "Fancy Feast Sliced Turkey Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_CHICKEN_FEAST_3_OZ": {
            "name": "Fancy Feast Chunky Chicken Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_CHICKEN_FEAST_5_5_OZ": {
            "name": "Fancy Feast Chunky Chicken Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_TURKEY_FEAST_3_OZ": {
            "name": "Fancy Feast Chunky Turkey Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_TURKEY_FEAST_5_5_OZ": {
            "name": "Fancy Feast Chunky Turkey Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_BEEF_FEAST_3_OZ": {
            "name": "Fancy Feast Chunky Beef Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CHUNKY_BEEF_FEAST_5_5_OZ": {
            "name": "Fancy Feast Chunky Beef Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_BEEF_LIVER_FEAST_3_OZ": {
            "name": "Fancy Feast Beef & Liver Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_BEEF_LIVER_FEAST_5_5_OZ": {
            "name": "Fancy Feast Beef & Liver Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CHICKEN_TUNA_FEAST_3_OZ": {
            "name": "Fancy Feast Chicken & Tuna Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CHICKEN_TUNA_FEAST_5_5_OZ": {
            "name": "Fancy Feast Chicken & Tuna Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_TUNA_CRAB_FEAST_3_OZ": {
            "name": "Fancy Feast Tuna & Crab Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_TUNA_CRAB_FEAST_5_5_OZ": {
            "name": "Fancy Feast Tuna & Crab Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_SALMON_SHRIMP_FEAST_3_OZ": {
            "name": "Fancy Feast Salmon & Shrimp Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_SALMON_SHRIMP_FEAST_5_5_OZ": {
            "name": "Fancy Feast Salmon & Shrimp Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_TROUT_FEAST_3_OZ": {
            "name": "Fancy Feast Trout Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_TROUT_FEAST_5_5_OZ": {
            "name": "Fancy Feast Trout Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_WILD_SALMON_SHRIMP_FEAST_3_OZ": {
            "name": "Fancy Feast Wild Salmon & Shrimp Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_WILD_SALMON_SHRIMP_FEAST_5_5_OZ": {
            "name": "Fancy Feast Wild Salmon & Shrimp Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_COD_SHRIMP_FEAST_3_OZ": {
            "name": "Fancy Feast Cod & Shrimp Feast Wet Cat Food, 3-oz cans (case 30)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_COD_SHRIMP_FEAST_5_5_OZ": {
            "name": "Fancy Feast Cod & Shrimp Feast Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_QUAIL_EGG_2_8_OZ": {
            "name": "Tiki Cat After Dark Chicken & Quail Egg Wet Cat Food, 2.8-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_QUAIL_EGG_6_OZ": {
            "name": "Tiki Cat After Dark Chicken & Quail Egg Wet Cat Food, 6-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_PORK_2_8_OZ": {
            "name": "Tiki Cat After Dark Chicken & Pork Wet Cat Food, 2.8-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_PORK_6_OZ": {
            "name": "Tiki Cat After Dark Chicken & Pork Wet Cat Food, 6-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_LAMB_2_8_OZ": {
            "name": "Tiki Cat After Dark Chicken & Lamb Wet Cat Food, 2.8-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_LAMB_6_OZ": {
            "name": "Tiki Cat After Dark Chicken & Lamb Wet Cat Food, 6-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_BEEF_2_8_OZ": {
            "name": "Tiki Cat After Dark Chicken & Beef Wet Cat Food, 2.8-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_BEEF_6_OZ": {
            "name": "Tiki Cat After Dark Chicken & Beef Wet Cat Food, 6-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_DUCK_2_8_OZ": {
            "name": "Tiki Cat After Dark Chicken & Duck Wet Cat Food, 2.8-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_TIKI_CAT_AFTER_DARK_CHICKEN_DUCK_6_OZ": {
            "name": "Tiki Cat After Dark Chicken & Duck Wet Cat Food, 6-oz cans (case 12)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_BLUE_BUFFALO_WILDERNESS_INDOOR_CHICKEN_RECIPE_GRAIN_FREE_5_LB": {
            "name": "Blue Buffalo Wilderness Indoor Chicken Recipe Grain-Free Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_BLUE_BUFFALO_WILDERNESS_INDOOR_CHICKEN_RECIPE_GRAIN_FREE_11_LB": {
            "name": "Blue Buffalo Wilderness Indoor Chicken Recipe Grain-Free Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_BLUE_BUFFALO_WILDERNESS_SALMON_RECIPE_GRAIN_FREE_5_LB": {
            "name": "Blue Buffalo Wilderness Salmon Recipe Grain-Free Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_BLUE_BUFFALO_WILDERNESS_SALMON_RECIPE_GRAIN_FREE_11_LB": {
            "name": "Blue Buffalo Wilderness Salmon Recipe Grain-Free Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_BLUE_BUFFALO_INDOOR_HAIRBALL_CHICKEN_BROWN_RICE_5_LB": {
            "name": "Blue Buffalo Indoor Hairball Chicken & Brown Rice Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_BLUE_BUFFALO_INDOOR_HAIRBALL_CHICKEN_BROWN_RICE_11_LB": {
            "name": "Blue Buffalo Indoor Hairball Chicken & Brown Rice Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_BLUE_BUFFALO_WEIGHT_CONTROL_CHICKEN_BROWN_RICE_5_LB": {
            "name": "Blue Buffalo Weight Control Chicken & Brown Rice Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_BLUE_BUFFALO_WEIGHT_CONTROL_CHICKEN_BROWN_RICE_11_LB": {
            "name": "Blue Buffalo Weight Control Chicken & Brown Rice Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_BLUE_BUFFALO_KITTEN_CHICKEN_RECIPE_GRAIN_FREE_5_LB": {
            "name": "Blue Buffalo Kitten Chicken Recipe Grain-Free Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_BLUE_BUFFALO_KITTEN_CHICKEN_RECIPE_GRAIN_FREE_11_LB": {
            "name": "Blue Buffalo Kitten Chicken Recipe Grain-Free Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_PURINA_PRO_PLAN_SALMON_RICE_ENTR_E_IN_SAUCE_3_OZ": {
            "name": "Purina Pro Plan Salmon & Rice Entree in Sauce Wet Cat Food, 3-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_PURINA_PRO_PLAN_CHICKEN_RICE_ENTR_E_IN_SAUCE_3_OZ": {
            "name": "Purina Pro Plan Chicken & Rice Entree in Sauce Wet Cat Food, 3-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_PURINA_PRO_PLAN_TUNA_RICE_ENTR_E_IN_SAUCE_3_OZ": {
            "name": "Purina Pro Plan Tuna & Rice Entree in Sauce Wet Cat Food, 3-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_PURINA_PRO_PLAN_TURKEY_RICE_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Purina Pro Plan Turkey & Rice Entree in Gravy Wet Cat Food, 3-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_PURINA_PRO_PLAN_LAMB_VEGETABLES_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Purina Pro Plan Lamb & Vegetables Entree in Gravy Wet Cat Food, 3-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_HILL_S_SCIENCE_DIET_ADULT_CHICKEN_ENTR_E_5_5_OZ": {
            "name": "Hill's Science Diet Adult Chicken Entree Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_HILL_S_SCIENCE_DIET_ADULT_TURKEY_LIVER_ENTR_E_5_5_OZ": {
            "name": "Hill's Science Diet Adult Turkey & Liver Entree Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_HILL_S_SCIENCE_DIET_ADULT_OCEAN_FISH_ENTR_E_5_5_OZ": {
            "name": "Hill's Science Diet Adult Ocean Fish Entree Wet Cat Food, 5.5-oz cans (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_ROYAL_CANIN_INDOOR_ADULT_3_LB": {
            "name": "Royal Canin Indoor Adult Dry Cat Food, 3-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_ROYAL_CANIN_INDOOR_ADULT_7_LB": {
            "name": "Royal Canin Indoor Adult Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_ROYAL_CANIN_INDOOR_ADULT_15_LB": {
            "name": "Royal Canin Indoor Adult Dry Cat Food, 15-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_IAMS_PERFECT_PORTIONS_INDOOR_CHICKEN_PAT_2_6_OZ": {
            "name": "Iams Perfect Portions Indoor Chicken Pate Wet Cat Food, 2.6-oz twin-packs (case 24)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_CHICKEN_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Chicken Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TENDER_BEEF_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Tender Beef Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_TURKEY_GIBLETS_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Turkey & Giblets Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_LIVER_CHICKEN_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Liver & Chicken Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_SALMON_SHRIMP_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Salmon & Shrimp Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_CLASSIC_PATE_OCEAN_WHITEFISH_TUNA_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Classic Pate Ocean Whitefish & Tuna Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_CHICKEN_FEAST_IN_GRAVY_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Grilled Chicken Feast in Gravy Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SALMON_FEAST_IN_GRAVY_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Grilled Salmon Feast in Gravy Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_TUNA_FEAST_IN_GRAVY_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Grilled Tuna Feast in Gravy Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_GRILLED_SEAFOOD_FEAST_VARIETY_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Grilled Seafood Feast Variety Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_CHICKEN_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Gravy Lovers Chicken Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_GRAVY_LOVERS_TURKEY_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Gravy Lovers Turkey Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_FLAKED_TUNA_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Flaked Tuna Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_PRIMAVERA_CHICKEN_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Medleys Primavera Chicken Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_TUSCANY_SALMON_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Medleys Tuscany Salmon Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_MEDLEYS_FLORENTINE_TUNA_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Medleys Florentine Tuna Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_CHICKEN_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Creamy Delights Chicken Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_CREAMY_DELIGHTS_SALMON_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Creamy Delights Salmon Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_BEEF_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Sliced Beef Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_SLICED_TURKEY_FEAST_VARIETY_PACK_3_OZ": {
            "name": "Fancy Feast Sliced Turkey Feast Variety Pack Wet Cat Food, 3-oz cans (variety 12-pack)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_BLUE_BUFFALO_TASTEFULS_CHICKEN_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Blue Buffalo Tastefuls Chicken Entree in Gravy Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_BLUE_BUFFALO_TASTEFULS_TURKEY_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Blue Buffalo Tastefuls Turkey Entree in Gravy Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_BLUE_BUFFALO_TASTEFULS_SALMON_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Blue Buffalo Tastefuls Salmon Entree in Gravy Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_BLUE_BUFFALO_TASTEFULS_TUNA_ENTR_E_IN_GRAVY_3_OZ": {
            "name": "Blue Buffalo Tastefuls Tuna Entree in Gravy Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_PURINA_ONE_INDOOR_ADVANTAGE_3_5_LB": {
            "name": "Purina One Indoor Advantage Dry Cat Food, 3.5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_PURINA_ONE_INDOOR_ADVANTAGE_7_LB": {
            "name": "Purina One Indoor Advantage Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_PURINA_ONE_INDOOR_ADVANTAGE_16_LB": {
            "name": "Purina One Indoor Advantage Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_PURINA_ONE_SENSITIVE_SKIN_STOMACH_3_5_LB": {
            "name": "Purina One Sensitive Skin & Stomach Dry Cat Food, 3.5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_PURINA_ONE_SENSITIVE_SKIN_STOMACH_7_LB": {
            "name": "Purina One Sensitive Skin & Stomach Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_PURINA_ONE_SENSITIVE_SKIN_STOMACH_16_LB": {
            "name": "Purina One Sensitive Skin & Stomach Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_PURINA_ONE_URINARY_TRACT_HEALTH_3_5_LB": {
            "name": "Purina One Urinary Tract Health Dry Cat Food, 3.5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_PURINA_ONE_URINARY_TRACT_HEALTH_7_LB": {
            "name": "Purina One Urinary Tract Health Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_PURINA_ONE_URINARY_TRACT_HEALTH_16_LB": {
            "name": "Purina One Urinary Tract Health Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_PURINA_ONE_HEALTHY_WEIGHT_3_5_LB": {
            "name": "Purina One Healthy Weight Dry Cat Food, 3.5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_PURINA_ONE_HEALTHY_WEIGHT_7_LB": {
            "name": "Purina One Healthy Weight Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_PURINA_ONE_HEALTHY_WEIGHT_16_LB": {
            "name": "Purina One Healthy Weight Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_PURINA_ONE_HAIRBALL_WEIGHT_CONTROL_3_5_LB": {
            "name": "Purina One Hairball & Weight Control Dry Cat Food, 3.5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_PURINA_ONE_HAIRBALL_WEIGHT_CONTROL_7_LB": {
            "name": "Purina One Hairball & Weight Control Dry Cat Food, 7-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_PURINA_ONE_HAIRBALL_WEIGHT_CONTROL_16_LB": {
            "name": "Purina One Hairball & Weight Control Dry Cat Food, 16-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_4_LB": {
            "name": "Orijen Original Grain-Free Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_8_LB": {
            "name": "Orijen Original Grain-Free Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_12_LB": {
            "name": "Orijen Original Grain-Free Dry Cat Food, 12-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_4_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_8_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_12_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Cat Food, 12-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_4_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_8_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_12_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Cat Food, 12-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_4_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_8_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_12_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Cat Food, 12-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_ORIJEN_TUNDRA_GRAIN_FREE_4_LB": {
            "name": "Orijen Tundra Grain-Free Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_ORIJEN_TUNDRA_GRAIN_FREE_8_LB": {
            "name": "Orijen Tundra Grain-Free Dry Cat Food, 8-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_ORIJEN_TUNDRA_GRAIN_FREE_12_LB": {
            "name": "Orijen Tundra Grain-Free Dry Cat Food, 12-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_CHICKEN_RICE_5_LB": {
            "name": "Wellness Complete Health Adult Chicken & Rice Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_CHICKEN_RICE_11_LB": {
            "name": "Wellness Complete Health Adult Chicken & Rice Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_WELLNESS_COMPLETE_HEALTH_INDOOR_SALMON_HERRING_5_LB": {
            "name": "Wellness Complete Health Indoor Salmon & Herring Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_WELLNESS_COMPLETE_HEALTH_INDOOR_SALMON_HERRING_11_LB": {
            "name": "Wellness Complete Health Indoor Salmon & Herring Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_WELLNESS_CORE_GRAIN_FREE_INDOOR_5_LB": {
            "name": "Wellness Core Grain-Free Indoor Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_WELLNESS_CORE_GRAIN_FREE_INDOOR_11_LB": {
            "name": "Wellness Core Grain-Free Indoor Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_WELLNESS_CORE_GRAIN_FREE_TURKEY_DUCK_5_LB": {
            "name": "Wellness Core Grain-Free Turkey & Duck Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_WELLNESS_CORE_GRAIN_FREE_TURKEY_DUCK_11_LB": {
            "name": "Wellness Core Grain-Free Turkey & Duck Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_WELLNESS_CORE_KITTEN_TURKEY_CHICKEN_5_LB": {
            "name": "Wellness Core Kitten Turkey & Chicken Dry Cat Food, 5-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_WELLNESS_CORE_KITTEN_TURKEY_CHICKEN_11_LB": {
            "name": "Wellness Core Kitten Turkey & Chicken Dry Cat Food, 11-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_BFF_OMG_GRAVY_CHICKEN_SALMON_2_8_OZ": {
            "name": "BFF OMG Gravy! Chicken & Salmon Wet Cat Food, 2.8-oz pouch (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_BFF_OMG_GRAVY_TUNA_SHRIMP_2_8_OZ": {
            "name": "BFF OMG Gravy! Tuna & Shrimp Wet Cat Food, 2.8-oz pouch (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_BFF_OMG_GRAVY_CHICKEN_LAMB_2_8_OZ": {
            "name": "BFF OMG Gravy! Chicken & Lamb Wet Cat Food, 2.8-oz pouch (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_BFF_OMG_GRAVY_DUCK_SALMON_2_8_OZ": {
            "name": "BFF OMG Gravy! Duck & Salmon Wet Cat Food, 2.8-oz pouch (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_BFF_OMG_GRAVY_BEEF_CHICKEN_2_8_OZ": {
            "name": "BFF OMG Gravy! Beef & Chicken Wet Cat Food, 2.8-oz pouch (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_TIKI_CAT_ALOHA_FRIENDS_TUNA_PUMPKIN_2_8_OZ": {
            "name": "Tiki Cat Aloha Friends Tuna & Pumpkin Wet Cat Food, 2.8-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_TIKI_CAT_ALOHA_FRIENDS_TUNA_PUMPKIN_6_OZ": {
            "name": "Tiki Cat Aloha Friends Tuna & Pumpkin Wet Cat Food, 6-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_TIKI_CAT_ALOHA_FRIENDS_CHICKEN_SHRIMP_2_8_OZ": {
            "name": "Tiki Cat Aloha Friends Chicken & Shrimp Wet Cat Food, 2.8-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_TIKI_CAT_ALOHA_FRIENDS_CHICKEN_SHRIMP_6_OZ": {
            "name": "Tiki Cat Aloha Friends Chicken & Shrimp Wet Cat Food, 6-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_EGG_2_8_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Egg Wet Cat Food, 2.8-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_EGG_6_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Egg Wet Cat Food, 6-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_LIVER_2_8_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Liver Wet Cat Food, 2.8-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_LIVER_6_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Liver Wet Cat Food, 6-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_DUCK_2_8_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Duck Wet Cat Food, 2.8-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_TIKI_CAT_BORN_CARNIVORE_CHICKEN_DUCK_6_OZ": {
            "name": "Tiki Cat Born Carnivore Chicken & Duck Wet Cat Food, 6-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_ROASTED_TURKEY_ENTR_E_P_T_3_OZ": {
            "name": "Fancy Feast Petites Roasted Turkey Entree Pate Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_ROASTED_TURKEY_ENTR_E_P_T_5_5_OZ": {
            "name": "Fancy Feast Petites Roasted Turkey Entree Pate Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_BRAISED_CHICKEN_ENTR_E_P_T_3_OZ": {
            "name": "Fancy Feast Petites Braised Chicken Entree Pate Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_BRAISED_CHICKEN_ENTR_E_P_T_5_5_OZ": {
            "name": "Fancy Feast Petites Braised Chicken Entree Pate Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_OCEAN_WHITEFISH_ENTR_E_P_T_3_OZ": {
            "name": "Fancy Feast Petites Ocean Whitefish Entree Pate Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_OCEAN_WHITEFISH_ENTR_E_P_T_5_5_OZ": {
            "name": "Fancy Feast Petites Ocean Whitefish Entree Pate Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_GRILLED_CHICKEN_ENTR_E_3_OZ": {
            "name": "Fancy Feast Petites Grilled Chicken Entree Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_GRILLED_CHICKEN_ENTR_E_5_5_OZ": {
            "name": "Fancy Feast Petites Grilled Chicken Entree Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_SEARED_SALMON_ENTR_E_3_OZ": {
            "name": "Fancy Feast Petites Seared Salmon Entree Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_PETITES_SEARED_SALMON_ENTR_E_5_5_OZ": {
            "name": "Fancy Feast Petites Seared Salmon Entree Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_PURELY_NATURAL_SKIPJACK_TUNA_SALMON_3_OZ": {
            "name": "Fancy Feast Purely Natural Skipjack Tuna & Salmon Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_PURELY_NATURAL_SKIPJACK_TUNA_SALMON_5_5_OZ": {
            "name": "Fancy Feast Purely Natural Skipjack Tuna & Salmon Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_PURELY_NATURAL_WILD_ALASKAN_SALMON_3_OZ": {
            "name": "Fancy Feast Purely Natural Wild Alaskan Salmon Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_PURELY_NATURAL_WILD_ALASKAN_SALMON_5_5_OZ": {
            "name": "Fancy Feast Purely Natural Wild Alaskan Salmon Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_CHICKEN_VEGETABLES_3_OZ": {
            "name": "Fancy Feast Broths Classic Chicken & Vegetables Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_CHICKEN_VEGETABLES_5_5_OZ": {
            "name": "Fancy Feast Broths Classic Chicken & Vegetables Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_TUNA_VEGETABLES_3_OZ": {
            "name": "Fancy Feast Broths Classic Tuna & Vegetables Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_TUNA_VEGETABLES_5_5_OZ": {
            "name": "Fancy Feast Broths Classic Tuna & Vegetables Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_SEAFOOD_VEGETABLES_3_OZ": {
            "name": "Fancy Feast Broths Classic Seafood & Vegetables Wet Cat Food, 3-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_FANCY_FEAST_BROTHS_CLASSIC_SEAFOOD_VEGETABLES_5_5_OZ": {
            "name": "Fancy Feast Broths Classic Seafood & Vegetables Wet Cat Food, 5.5-oz can (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_ORIJEN_GUARDIAN_8_4_LB": {
            "name": "Orijen Guardian 8 Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_DRY_ORIJEN_GUARDIAN_8_10_LB": {
            "name": "Orijen Guardian 8 Dry Cat Food, 10-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_DRY_ORIJEN_INDOOR_CAT_4_LB": {
            "name": "Orijen Indoor Cat Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_DRY_ORIJEN_INDOOR_CAT_10_LB": {
            "name": "Orijen Indoor Cat Dry Cat Food, 10-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_DRY_ORIJEN_KITTEN_4_LB": {
            "name": "Orijen Kitten Dry Cat Food, 4-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 128.99
        },
        "CAT_DRY_ORIJEN_KITTEN_10_LB": {
            "name": "Orijen Kitten Dry Cat Food, 10-lb bag",
            "category": "Dry Cat Food (Non-Prescription)",
            "price": 38.99
        },
        "CAT_WET_NUTRO_PERFECT_PORTIONS_CUTS_IN_GRAVY_CHICKEN_2_6_OZ": {
            "name": "Nutro Perfect Portions Cuts in Gravy Chicken Wet Cat Food, 2.6-oz twin-pack (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 58.99
        },
        "CAT_WET_NUTRO_PERFECT_PORTIONS_CUTS_IN_GRAVY_SALMON_2_6_OZ": {
            "name": "Nutro Perfect Portions Cuts in Gravy Salmon Wet Cat Food, 2.6-oz twin-pack (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 78.99
        },
        "CAT_WET_NUTRO_PERFECT_PORTIONS_PAT_CHICKEN_LIVER_2_6_OZ": {
            "name": "Nutro Perfect Portions Pate Chicken & Liver Wet Cat Food, 2.6-oz twin-pack (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 98.99
        },
        "CAT_WET_NUTRO_PERFECT_PORTIONS_PAT_OCEANFISH_TUNA_2_6_OZ": {
            "name": "Nutro Perfect Portions Pate Oceanfish & Tuna Wet Cat Food, 2.6-oz twin-pack (single)",
            "category": "Wet Cat Food (Non-Prescription)",
            "price": 128.99
        },    
        "DOG_DRY_ACANA_FREE_RUN_POULTRY_GRAIN_FREE_4_LB": {
            "name": "Acana Free-Run Poultry Grain-Free Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ACANA_FREE_RUN_POULTRY_GRAIN_FREE_13_LB": {
            "name": "Acana Free-Run Poultry Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ACANA_FREE_RUN_POULTRY_GRAIN_FREE_25_LB": {
            "name": "Acana Free-Run Poultry Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ACANA_GRASSLANDS_GRAIN_FREE_4_LB": {
            "name": "Acana Grasslands Grain-Free Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ACANA_GRASSLANDS_GRAIN_FREE_13_LB": {
            "name": "Acana Grasslands Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_ACANA_GRASSLANDS_GRAIN_FREE_25_LB": {
            "name": "Acana Grasslands Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ACANA_WILD_ATLANTIC_GRAIN_FREE_4_LB": {
            "name": "Acana Wild Atlantic Grain-Free Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ACANA_WILD_ATLANTIC_GRAIN_FREE_13_LB": {
            "name": "Acana Wild Atlantic Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ACANA_WILD_ATLANTIC_GRAIN_FREE_25_LB": {
            "name": "Acana Wild Atlantic Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ACANA_MEADOWLAND_GRAIN_FREE_4_LB": {
            "name": "Acana Meadowland Grain-Free Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_ACANA_MEADOWLAND_GRAIN_FREE_13_LB": {
            "name": "Acana Meadowland Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ACANA_MEADOWLAND_GRAIN_FREE_25_LB": {
            "name": "Acana Meadowland Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ACANA_RED_MEAT_GRAIN_FREE_4_LB": {
            "name": "Acana Red Meat Grain-Free Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ACANA_RED_MEAT_GRAIN_FREE_13_LB": {
            "name": "Acana Red Meat Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ACANA_RED_MEAT_GRAIN_FREE_25_LB": {
            "name": "Acana Red Meat Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_4_5_LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_13_LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ORIJEN_ORIGINAL_GRAIN_FREE_25_LB": {
            "name": "Orijen Original Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ORIJEN_TUNDRA_GRAIN_FREE_4_5_LB": {
            "name": "Orijen Tundra Grain-Free Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ORIJEN_TUNDRA_GRAIN_FREE_13_LB": {
            "name": "Orijen Tundra Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_ORIJEN_TUNDRA_GRAIN_FREE_25_LB": {
            "name": "Orijen Tundra Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_4_5_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_13_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ORIJEN_REGIONAL_RED_GRAIN_FREE_25_LB": {
            "name": "Orijen Regional Red Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_4_5_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_13_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_ORIJEN_SIX_FISH_GRAIN_FREE_25_LB": {
            "name": "Orijen Six Fish Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_4_5_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_13_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Dog Food, 13-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_ORIJEN_FIT_TRIM_GRAIN_FREE_25_LB": {
            "name": "Orijen Fit & Trim Grain-Free Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_CHICKEN_BROWN_RICE_5_LB": {
            "name": "Blue Buffalo Life Protection Chicken & Brown Rice Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_CHICKEN_BROWN_RICE_15_LB": {
            "name": "Blue Buffalo Life Protection Chicken & Brown Rice Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_CHICKEN_BROWN_RICE_30_LB": {
            "name": "Blue Buffalo Life Protection Chicken & Brown Rice Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_LAMB_BROWN_RICE_5_LB": {
            "name": "Blue Buffalo Life Protection Lamb & Brown Rice Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_LAMB_BROWN_RICE_15_LB": {
            "name": "Blue Buffalo Life Protection Lamb & Brown Rice Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_LAMB_BROWN_RICE_30_LB": {
            "name": "Blue Buffalo Life Protection Lamb & Brown Rice Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_FISH_OATMEAL_5_LB": {
            "name": "Blue Buffalo Life Protection Fish & Oatmeal Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_FISH_OATMEAL_15_LB": {
            "name": "Blue Buffalo Life Protection Fish & Oatmeal Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_FISH_OATMEAL_30_LB": {
            "name": "Blue Buffalo Life Protection Fish & Oatmeal Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_HEALTHY_WEIGHT_CHICKEN_5_LB": {
            "name": "Blue Buffalo Life Protection Healthy Weight Chicken Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_HEALTHY_WEIGHT_CHICKEN_15_LB": {
            "name": "Blue Buffalo Life Protection Healthy Weight Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_BLUE_BUFFALO_LIFE_PROTECTION_HEALTHY_WEIGHT_CHICKEN_30_LB": {
            "name": "Blue Buffalo Life Protection Healthy Weight Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_SALMON_GRAIN_FREE_5_LB": {
            "name": "Blue Buffalo Wilderness Salmon Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_SALMON_GRAIN_FREE_15_LB": {
            "name": "Blue Buffalo Wilderness Salmon Grain-Free Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_BLUE_BUFFALO_WILDERNESS_SALMON_GRAIN_FREE_30_LB": {
            "name": "Blue Buffalo Wilderness Salmon Grain-Free Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_CHICKEN_RICE_6_LB": {
            "name": "Purina Pro Plan Shredded Blend Chicken & Rice Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_CHICKEN_RICE_18_LB": {
            "name": "Purina Pro Plan Shredded Blend Chicken & Rice Dry Dog Food, 18-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_CHICKEN_RICE_35_LB": {
            "name": "Purina Pro Plan Shredded Blend Chicken & Rice Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_LAMB_RICE_6_LB": {
            "name": "Purina Pro Plan Shredded Blend Lamb & Rice Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_LAMB_RICE_18_LB": {
            "name": "Purina Pro Plan Shredded Blend Lamb & Rice Dry Dog Food, 18-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_LAMB_RICE_35_LB": {
            "name": "Purina Pro Plan Shredded Blend Lamb & Rice Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_SALMON_RICE_6_LB": {
            "name": "Purina Pro Plan Shredded Blend Salmon & Rice Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_SALMON_RICE_18_LB": {
            "name": "Purina Pro Plan Shredded Blend Salmon & Rice Dry Dog Food, 18-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SHREDDED_BLEND_SALMON_RICE_35_LB": {
            "name": "Purina Pro Plan Shredded Blend Salmon & Rice Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SENSITIVE_SKIN_STOMACH_SALMON_RICE_6_LB": {
            "name": "Purina Pro Plan Sensitive Skin & Stomach Salmon & Rice Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SENSITIVE_SKIN_STOMACH_SALMON_RICE_18_LB": {
            "name": "Purina Pro Plan Sensitive Skin & Stomach Salmon & Rice Dry Dog Food, 18-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_SENSITIVE_SKIN_STOMACH_SALMON_RICE_35_LB": {
            "name": "Purina Pro Plan Sensitive Skin & Stomach Salmon & Rice Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_WEIGHT_MANAGEMENT_CHICKEN_RICE_6_LB": {
            "name": "Purina Pro Plan Weight Management Chicken & Rice Dry Dog Food, 6-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_WEIGHT_MANAGEMENT_CHICKEN_RICE_18_LB": {
            "name": "Purina Pro Plan Weight Management Chicken & Rice Dry Dog Food, 18-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_PURINA_PRO_PLAN_WEIGHT_MANAGEMENT_CHICKEN_RICE_35_LB": {
            "name": "Purina Pro Plan Weight Management Chicken & Rice Dry Dog Food, 35-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_CHICKEN_BARLEY_5_LB": {
            "name": "Hill's Science Diet Adult Chicken & Barley Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_CHICKEN_BARLEY_15_LB": {
            "name": "Hill's Science Diet Adult Chicken & Barley Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_CHICKEN_BARLEY_30_LB": {
            "name": "Hill's Science Diet Adult Chicken & Barley Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_LAMB_MEAL_BROWN_RICE_5_LB": {
            "name": "Hill's Science Diet Adult Lamb Meal & Brown Rice Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_LAMB_MEAL_BROWN_RICE_15_LB": {
            "name": "Hill's Science Diet Adult Lamb Meal & Brown Rice Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_ADULT_LAMB_MEAL_BROWN_RICE_30_LB": {
            "name": "Hill's Science Diet Adult Lamb Meal & Brown Rice Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_SENSITIVE_STOMACH_SKIN_CHICKEN_5_LB": {
            "name": "Hill's Science Diet Sensitive Stomach & Skin Chicken Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_SENSITIVE_STOMACH_SKIN_CHICKEN_15_LB": {
            "name": "Hill's Science Diet Sensitive Stomach & Skin Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_SENSITIVE_STOMACH_SKIN_CHICKEN_30_LB": {
            "name": "Hill's Science Diet Sensitive Stomach & Skin Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_LARGE_BREED_CHICKEN_BARLEY_5_LB": {
            "name": "Hill's Science Diet Large Breed Chicken & Barley Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_LARGE_BREED_CHICKEN_BARLEY_15_LB": {
            "name": "Hill's Science Diet Large Breed Chicken & Barley Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_LARGE_BREED_CHICKEN_BARLEY_30_LB": {
            "name": "Hill's Science Diet Large Breed Chicken & Barley Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_PUPPY_CHICKEN_MEAL_BARLEY_5_LB": {
            "name": "Hill's Science Diet Puppy Chicken Meal & Barley Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_PUPPY_CHICKEN_MEAL_BARLEY_15_LB": {
            "name": "Hill's Science Diet Puppy Chicken Meal & Barley Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_HILL_S_SCIENCE_DIET_PUPPY_CHICKEN_MEAL_BARLEY_30_LB": {
            "name": "Hill's Science Diet Puppy Chicken Meal & Barley Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_MERRICK_REAL_CHICKEN_SWEET_POTATO_4_LB": {
            "name": "Merrick Real Chicken & Sweet Potato Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_MERRICK_REAL_CHICKEN_SWEET_POTATO_12_LB": {
            "name": "Merrick Real Chicken & Sweet Potato Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_MERRICK_REAL_CHICKEN_SWEET_POTATO_25_LB": {
            "name": "MerricK Real Chicken & Sweet Potato Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_MERRICK_REAL_BEEF_SWEET_POTATO_4_LB": {
            "name": "Merrick Real Beef & Sweet Potato Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_MERRICK_REAL_BEEF_SWEET_POTATO_12_LB": {
            "name": "Merrick Real Beef & Sweet Potato Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_MERRICK_REAL_BEEF_SWEET_POTATO_25_LB": {
            "name": "Merrick Real Beef & Sweet Potato Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_MERRICK_REAL_SALMON_SWEET_POTATO_4_LB": {
            "name": "Merrick Real Salmon & Sweet Potato Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_MERRICK_REAL_SALMON_SWEET_POTATO_12_LB": {
            "name": "Merrick Real Salmon & Sweet Potato Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_MERRICK_REAL_SALMON_SWEET_POTATO_25_LB": {
            "name": "Merrick Real Salmon & Sweet Potato Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_MERRICK_TEXAS_BEEF_PORK_4_LB": {
            "name": "Merrick Texas Beef & Pork Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_MERRICK_TEXAS_BEEF_PORK_12_LB": {
            "name": "Merrick Texas Beef & Pork Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_MERRICK_TEXAS_BEEF_PORK_25_LB": {
            "name": "Merrick Texas Beef & Pork Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_MERRICK_HEALTHY_WEIGHT_CHICKEN_SWEET_POTATO_4_LB": {
            "name": "Merrick Healthy Weight Chicken & Sweet Potato Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_MERRICK_HEALTHY_WEIGHT_CHICKEN_SWEET_POTATO_12_LB": {
            "name": "Merrick Healthy Weight Chicken & Sweet Potato Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_MERRICK_HEALTHY_WEIGHT_CHICKEN_SWEET_POTATO_25_LB": {
            "name": "Merrick Healthy Weight Chicken & Sweet Potato Dry Dog Food, 25-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_WET_BLUE_BUFFALO_HOMESTYLE_RECIPE_CHICKEN_DINNER_12_5_OZ": {
            "name": "Blue Buffalo Homestyle Recipe Chicken Dinner Wet Dog Food, 12.5-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_WET_BLUE_BUFFALO_HOMESTYLE_RECIPE_BEEF_DINNER_12_5_OZ": {
            "name": "Blue Buffalo Homestyle Recipe Beef Dinner Wet Dog Food, 12.5-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_WET_BLUE_BUFFALO_HOMESTYLE_RECIPE_LAMB_DINNER_12_5_OZ": {
            "name": "Blue Buffalo Homestyle Recipe Lamb Dinner Wet Dog Food, 12.5-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_WET_BLUE_BUFFALO_WILDERNESS_SALMON_CHICKEN_GRILL_12_5_OZ": {
            "name": "Blue Buffalo Wilderness Salmon & Chicken Grill Wet Dog Food, 12.5-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_WET_BLUE_BUFFALO_WILDERNESS_BEEF_CHICKEN_GRILL_12_5_OZ": {
            "name": "Blue Buffalo Wilderness Beef & Chicken Grill Wet Dog Food, 12.5-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_WET_PURINA_BENEFUL_PREPARED_MEALS_CHICKEN_STEW_10_OZ": {
            "name": "Purina Beneful Prepared Meals Chicken Stew Wet Dog Food, 10-oz tubs (case 8)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_WET_PURINA_BENEFUL_PREPARED_MEALS_BEEF_STEW_10_OZ": {
            "name": "Purina Beneful Prepared Meals Beef Stew Wet Dog Food, 10-oz tubs (case 8)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_WET_PURINA_BENEFUL_PREPARED_MEALS_POT_ROAST_10_OZ": {
            "name": "Purina Beneful Prepared Meals Pot Roast Wet Dog Food, 10-oz tubs (case 8)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_WET_PURINA_BENEFUL_PREPARED_MEALS_SAVORY_RICE_LAMB_10_OZ": {
            "name": "Purina Beneful Prepared Meals Savory Rice & Lamb Wet Dog Food, 10-oz tubs (case 8)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_WET_PURINA_BENEFUL_INCREDIBITES_CHICKEN_BEEF_STEW_10_OZ": {
            "name": "Purina Beneful IncrediBites Chicken & Beef Stew Wet Dog Food, 10-oz tubs (case 8)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_WET_HILL_S_SCIENCE_DIET_SAVORY_STEW_CHICKEN_VEGETABLES_12_8_OZ": {
            "name": "Hill's Science Diet Savory Stew Chicken & Vegetables Wet Dog Food, 12.8-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_WET_HILL_S_SCIENCE_DIET_SAVORY_STEW_BEEF_VEGETABLES_12_8_OZ": {
            "name": "Hill's Science Diet Savory Stew Beef & Vegetables Wet Dog Food, 12.8-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_WET_HILL_S_SCIENCE_DIET_SAVORY_STEW_TURKEY_VEGETABLES_12_8_OZ": {
            "name": "Hill's Science Diet Savory Stew Turkey & Vegetables Wet Dog Food, 12.8-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_WET_HILL_S_SCIENCE_DIET_ADULT_CHICKEN_BARLEY_ENTR_E_12_8_OZ": {
            "name": "Hill's Science Diet Adult Chicken & Barley Entree Wet Dog Food, 12.8-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_WET_HILL_S_SCIENCE_DIET_ADULT_BEEF_BARLEY_ENTR_E_12_8_OZ": {
            "name": "Hill's Science Diet Adult Beef & Barley Entree Wet Dog Food, 12.8-oz cans (case 12)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_WELLNESS_CORE_ORIGINAL_DEBONED_TURKEY_CHICKEN_4_LB": {
            "name": "Wellness Core Original Deboned Turkey & Chicken Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_WELLNESS_CORE_ORIGINAL_DEBONED_TURKEY_CHICKEN_12_LB": {
            "name": "Wellness Core Original Deboned Turkey & Chicken Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_WELLNESS_CORE_ORIGINAL_DEBONED_TURKEY_CHICKEN_26_LB": {
            "name": "Wellness Core Original Deboned Turkey & Chicken Dry Dog Food, 26-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_WELLNESS_CORE_OCEAN_WHITEFISH_HERRING_SALMON_4_LB": {
            "name": "Wellness Core Ocean Whitefish, Herring & Salmon Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_WELLNESS_CORE_OCEAN_WHITEFISH_HERRING_SALMON_12_LB": {
            "name": "Wellness Core Ocean Whitefish, Herring & Salmon Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_WELLNESS_CORE_OCEAN_WHITEFISH_HERRING_SALMON_26_LB": {
            "name": "Wellness Core Ocean Whitefish, Herring & Salmon Dry Dog Food, 26-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_CHICKEN_OATMEAL_4_LB": {
            "name": "Wellness Complete Health Adult Chicken & Oatmeal Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_CHICKEN_OATMEAL_12_LB": {
            "name": "Wellness Complete Health Adult Chicken & Oatmeal Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_CHICKEN_OATMEAL_26_LB": {
            "name": "Wellness Complete Health Adult Chicken & Oatmeal Dry Dog Food, 26-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_LAMB_BARLEY_4_LB": {
            "name": "Wellness Complete Health Adult Lamb & Barley Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_LAMB_BARLEY_12_LB": {
            "name": "Wellness Complete Health Adult Lamb & Barley Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_ADULT_LAMB_BARLEY_26_LB": {
            "name": "Wellness Complete Health Adult Lamb & Barley Dry Dog Food, 26-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_HEALTHY_WEIGHT_4_LB": {
            "name": "Wellness Complete Health Healthy Weight Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_HEALTHY_WEIGHT_12_LB": {
            "name": "Wellness Complete Health Healthy Weight Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_WELLNESS_COMPLETE_HEALTH_HEALTHY_WEIGHT_26_LB": {
            "name": "Wellness Complete Health Healthy Weight Dry Dog Food, 26-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_NULO_FREESTYLE_SALMON_PEAS_4_5_LB": {
            "name": "Nulo Freestyle Salmon & Peas Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_NULO_FREESTYLE_SALMON_PEAS_11_LB": {
            "name": "Nulo Freestyle Salmon & Peas Dry Dog Food, 11-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_NULO_FREESTYLE_SALMON_PEAS_24_LB": {
            "name": "Nulo Freestyle Salmon & Peas Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_NULO_FREESTYLE_TURKEY_SWEET_POTATO_4_5_LB": {
            "name": "Nulo Freestyle Turkey & Sweet Potato Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_NULO_FREESTYLE_TURKEY_SWEET_POTATO_11_LB": {
            "name": "Nulo Freestyle Turkey & Sweet Potato Dry Dog Food, 11-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_NULO_FREESTYLE_TURKEY_SWEET_POTATO_24_LB": {
            "name": "Nulo Freestyle Turkey & Sweet Potato Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_NULO_FREESTYLE_BEEF_PEAR_LENTILS_LIMITED_4_5_LB": {
            "name": "Nulo Freestyle Beef, Pear & Lentils Limited+ Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_NULO_FREESTYLE_BEEF_PEAR_LENTILS_LIMITED_11_LB": {
            "name": "Nulo Freestyle Beef, Pear & Lentils Limited+ Dry Dog Food, 11-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_NULO_FREESTYLE_BEEF_PEAR_LENTILS_LIMITED_24_LB": {
            "name": "Nulo Freestyle Beef, Pear & Lentils Limited+ Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_NULO_FREESTYLE_LAMB_CHICKPEAS_4_5_LB": {
            "name": "Nulo Freestyle Lamb & Chickpeas Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_NULO_FREESTYLE_LAMB_CHICKPEAS_11_LB": {
            "name": "Nulo Freestyle Lamb & Chickpeas Dry Dog Food, 11-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_NULO_FREESTYLE_LAMB_CHICKPEAS_24_LB": {
            "name": "Nulo Freestyle Lamb & Chickpeas Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_NULO_FREESTYLE_COD_LENTILS_LIMITED_4_5_LB": {
            "name": "Nulo Freestyle Cod & Lentils Limited+ Dry Dog Food, 4.5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_NULO_FREESTYLE_COD_LENTILS_LIMITED_11_LB": {
            "name": "Nulo Freestyle Cod & Lentils Limited+ Dry Dog Food, 11-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_NULO_FREESTYLE_COD_LENTILS_LIMITED_24_LB": {
            "name": "Nulo Freestyle Cod & Lentils Limited+ Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_WET_CESAR_CLASSIC_LOAF_IN_SAUCE_FILET_MIGNON_3_5_OZ": {
            "name": "Cesar Classic Loaf in Sauce Filet Mignon Wet Dog Food, 3.5-oz tray (single)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_WET_CESAR_CLASSIC_LOAF_IN_SAUCE_PORTERHOUSE_STEAK_3_5_OZ": {
            "name": "Cesar Classic Loaf in Sauce Porterhouse Steak Wet Dog Food, 3.5-oz tray (single)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_WET_CESAR_CLASSIC_LOAF_IN_SAUCE_CHICKEN_LIVER_3_5_OZ": {
            "name": "Cesar Classic Loaf in Sauce Chicken & Liver Wet Dog Food, 3.5-oz tray (single)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_WET_CESAR_HOME_DELIGHTS_SLOW_COOKED_CHICKEN_VEGETABLE_3_5_OZ": {
            "name": "Cesar Home Delights Slow Cooked Chicken & Vegetable Wet Dog Food, 3.5-oz tray (single)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_WET_CESAR_SAVORY_DELIGHTS_ROTISSERIE_CHICKEN_BACON_CHEESE_3_5_OZ": {
            "name": "Cesar Savory Delights Rotisserie Chicken Bacon & Cheese Wet Dog Food, 3.5-oz tray (single)",
            "category": "Wet Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_SALMON_SWEET_POTATO_4_LB": {
            "name": "CANIDAE PURE Real Salmon & Sweet Potato Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_SALMON_SWEET_POTATO_12_LB": {
            "name": "CANIDAE PURE Real Salmon & Sweet Potato Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_SALMON_SWEET_POTATO_24_LB": {
            "name": "CANIDAE PURE Real Salmon & Sweet Potato Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_BISON_LENTIL_CARROT_4_LB": {
            "name": "CANIDAE PURE Real Bison, Lentil & Carrot Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_BISON_LENTIL_CARROT_12_LB": {
            "name": "CANIDAE PURE Real Bison, Lentil & Carrot Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_BISON_LENTIL_CARROT_24_LB": {
            "name": "CANIDAE PURE Real Bison, Lentil & Carrot Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_LAMB_PEA_4_LB": {
            "name": "CANIDAE PURE Real Lamb & Pea Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_LAMB_PEA_12_LB": {
            "name": "CANIDAE PURE Real Lamb & Pea Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_CANIDAE_PURE_REAL_LAMB_PEA_24_LB": {
            "name": "CANIDAE PURE Real Lamb & Pea Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_CHICKEN_RICE_4_LB": {
            "name": "CANIDAE All Life Stages Chicken & Rice Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_CHICKEN_RICE_12_LB": {
            "name": "CANIDAE All Life Stages Chicken & Rice Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_CHICKEN_RICE_24_LB": {
            "name": "CANIDAE All Life Stages Chicken & Rice Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_LAMB_RICE_4_LB": {
            "name": "CANIDAE All Life Stages Lamb & Rice Dry Dog Food, 4-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_LAMB_RICE_12_LB": {
            "name": "CANIDAE All Life Stages Lamb & Rice Dry Dog Food, 12-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_CANIDAE_ALL_LIFE_STAGES_LAMB_RICE_24_LB": {
            "name": "CANIDAE All Life Stages Lamb & Rice Dry Dog Food, 24-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_PACIFIC_STREAM_GRAIN_FREE_5_LB": {
            "name": "TASTE OF THE WILD Pacific Stream Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_PACIFIC_STREAM_GRAIN_FREE_14_LB": {
            "name": "TASTE OF THE WILD Pacific Stream Grain-Free Dry Dog Food, 14-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_PACIFIC_STREAM_GRAIN_FREE_28_LB": {
            "name": "TASTE OF THE WILD Pacific Stream Grain-Free Dry Dog Food, 28-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SIERRA_MOUNTAIN_GRAIN_FREE_5_LB": {
            "name": "TASTE OF THE WILD Sierra Mountain Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SIERRA_MOUNTAIN_GRAIN_FREE_14_LB": {
            "name": "TASTE OF THE WILD Sierra Mountain Grain-Free Dry Dog Food, 14-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SIERRA_MOUNTAIN_GRAIN_FREE_28_LB": {
            "name": "TASTE OF THE WILD Sierra Mountain Grain-Free Dry Dog Food, 28-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SOUTHWEST_CANYON_GRAIN_FREE_5_LB": {
            "name": "TASTE OF THE WILD Southwest Canyon Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SOUTHWEST_CANYON_GRAIN_FREE_14_LB": {
            "name": "TASTE OF THE WILD Southwest Canyon Grain-Free Dry Dog Food, 14-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_SOUTHWEST_CANYON_GRAIN_FREE_28_LB": {
            "name": "TASTE OF THE WILD Southwest Canyon Grain-Free Dry Dog Food, 28-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_WETLANDS_GRAIN_FREE_5_LB": {
            "name": "TASTE OF THE WILD Wetlands Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_WETLANDS_GRAIN_FREE_14_LB": {
            "name": "TASTE OF THE WILD Wetlands Grain-Free Dry Dog Food, 14-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_WETLANDS_GRAIN_FREE_28_LB": {
            "name": "TASTE OF THE WILD Wetlands Grain-Free Dry Dog Food, 28-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_HIGH_PRAIRIE_GRAIN_FREE_5_LB": {
            "name": "TASTE OF THE WILD High Prairie Grain-Free Dry Dog Food, 5-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_HIGH_PRAIRIE_GRAIN_FREE_14_LB": {
            "name": "TASTE OF THE WILD High Prairie Grain-Free Dry Dog Food, 14-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_TASTE_OF_THE_WILD_HIGH_PRAIRIE_GRAIN_FREE_28_LB": {
            "name": "TASTE OF THE WILD High Prairie Grain-Free Dry Dog Food, 28-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_ADULT_CHICKEN_7_LB": {
            "name": "IAMS ProActive Health Adult Chicken Dry Dog Food, 7-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_ADULT_CHICKEN_15_LB": {
            "name": "IAMS ProActive Health Adult Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_ADULT_CHICKEN_30_LB": {
            "name": "IAMS ProActive Health Adult Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_LARGE_BREED_CHICKEN_7_LB": {
            "name": "IAMS ProActive Health Large Breed Chicken Dry Dog Food, 7-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_LARGE_BREED_CHICKEN_15_LB": {
            "name": "IAMS ProActive Health Large Breed Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_LARGE_BREED_CHICKEN_30_LB": {
            "name": "IAMS ProActive Health Large Breed Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_HEALTHY_WEIGHT_7_LB": {
            "name": "IAMS ProActive Health Healthy Weight Dry Dog Food, 7-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_HEALTHY_WEIGHT_15_LB": {
            "name": "IAMS ProActive Health Healthy Weight Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_IAMS_PROACTIVE_HEALTH_HEALTHY_WEIGHT_30_LB": {
            "name": "IAMS ProActive Health Healthy Weight Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_SKIN_COAT_CHICKEN_7_LB": {
            "name": "IAMS Advanced Health Skin & Coat Chicken Dry Dog Food, 7-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_SKIN_COAT_CHICKEN_15_LB": {
            "name": "IAMS Advanced Health Skin & Coat Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 38.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_SKIN_COAT_CHICKEN_30_LB": {
            "name": "IAMS Advanced Health Skin & Coat Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 58.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_JOINT_CHICKEN_7_LB": {
            "name": "IAMS Advanced Health Joint Chicken Dry Dog Food, 7-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 78.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_JOINT_CHICKEN_15_LB": {
            "name": "IAMS Advanced Health Joint Chicken Dry Dog Food, 15-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 98.99
        },
        "DOG_DRY_IAMS_ADVANCED_HEALTH_JOINT_CHICKEN_30_LB": {
            "name": "IAMS Advanced Health Joint Chicken Dry Dog Food, 30-lb bag",
            "category": "Dry Dog Food (Non-Prescription)",
            "price": 128.99
        }
    }

    @classmethod
    def all(cls) -> Dict[str, Dict[str, Any]]:
        return cls._PRODUCTS

    @classmethod
    def get(cls, sku: str) -> Dict[str, Any] | None:
        return cls._PRODUCTS.get(sku)

    @classmethod
    def keys(cls) -> List[str]:
        return list(cls._PRODUCTS.keys())

PRODUCT_CATALOG: Dict[str, Dict[str, Any]] = ProductCatalog._PRODUCTS