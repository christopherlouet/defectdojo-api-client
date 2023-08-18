from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_settings_request_jira_minimum_severity import SystemSettingsRequestJiraMinimumSeverity
from ..models.system_settings_request_time_zone import SystemSettingsRequestTimeZone
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemSettingsRequest")


@_attrs_define
class SystemSettingsRequest:
    r"""
    Attributes:
        enable_auditlog (Union[Unset, bool]): With this setting turned on, Dojo maintains an audit log of changes made
            to entities (Findings, Tests, Engagements, Procuts, ...)If you run big import you may want to disable this
            because the way django-auditlog currently works, there's a big performance hit. Especially during (re-)imports.
        enable_deduplication (Union[Unset, bool]): With this setting turned on, Dojo deduplicates findings by comparing
            endpoints, cwe fields, and titles. If two findings share a URL and have the same CWE or title, Dojo marks the
            less recent finding as a duplicate. When deduplication is enabled, a list of deduplicated findings is added to
            the engagement view.
        delete_duplicates (Union[Unset, bool]): Requires next setting: maximum number of duplicates to retain.
        max_dupes (Union[Unset, None, int]): When enabled, if a single issue reaches the maximum number of duplicates,
            the oldest will be deleted. Duplicate will not be deleted when left empty. A value of 0 will remove all
            duplicates.
        email_from (Union[Unset, str]):
        enable_jira (Union[Unset, bool]):
        enable_jira_web_hook (Union[Unset, bool]): Please note: It is strongly recommended to use a secret below and /
            or IP whitelist the JIRA server using a proxy such as Nginx.
        disable_jira_webhook_secret (Union[Unset, bool]): Allows incoming requests without a secret (discouraged legacy
            behaviour)
        jira_webhook_secret (Union[Unset, None, str]): Secret needed in URL for incoming JIRA Webhook
        jira_minimum_severity (Union[Unset, None, SystemSettingsRequestJiraMinimumSeverity]): * `Critical` - Critical
            * `High` - High
            * `Medium` - Medium
            * `Low` - Low
            * `Info` - Info
        jira_labels (Union[Unset, None, str]): JIRA issue labels space seperated
        add_vulnerability_id_to_jira_label (Union[Unset, bool]):
        enable_github (Union[Unset, bool]):
        enable_slack_notifications (Union[Unset, bool]):
        slack_channel (Union[Unset, str]): Optional. Needed if you want to send global notifications.
        slack_token (Union[Unset, str]): Token required for interacting with Slack. Get one at
            https://api.slack.com/tokens
        slack_username (Union[Unset, str]): Optional. Will take your bot name otherwise.
        enable_msteams_notifications (Union[Unset, bool]):
        msteams_url (Union[Unset, str]): The full URL of the incoming webhook
        enable_mail_notifications (Union[Unset, bool]):
        mail_notifications_to (Union[Unset, str]):
        false_positive_history (Union[Unset, bool]): (EXPERIMENTAL) DefectDojo will automatically mark the finding as a
            false positive if an equal finding (according to its dedupe algorithm) has been previously marked as a false
            positive on the same product. ATTENTION: Although the deduplication algorithm is used to determine if a finding
            should be marked as a false positive, this feature will not work if deduplication is enabled since it doesn't
            make sense to use both.
        retroactive_false_positive_history (Union[Unset, bool]): (EXPERIMENTAL) FP History will also retroactively
            mark/unmark all existing equal findings in the same product as a false positives. Only works if the False
            Positive History feature is also enabled.
        url_prefix (Union[Unset, str]): URL prefix if DefectDojo is installed in it's own virtual subdirectory.
        team_name (Union[Unset, str]):
        time_zone (Union[Unset, SystemSettingsRequestTimeZone]): * `Africa/Abidjan` - Africa/Abidjan
            * `Africa/Accra` - Africa/Accra
            * `Africa/Addis_Ababa` - Africa/Addis_Ababa
            * `Africa/Algiers` - Africa/Algiers
            * `Africa/Asmara` - Africa/Asmara
            * `Africa/Asmera` - Africa/Asmera
            * `Africa/Bamako` - Africa/Bamako
            * `Africa/Bangui` - Africa/Bangui
            * `Africa/Banjul` - Africa/Banjul
            * `Africa/Bissau` - Africa/Bissau
            * `Africa/Blantyre` - Africa/Blantyre
            * `Africa/Brazzaville` - Africa/Brazzaville
            * `Africa/Bujumbura` - Africa/Bujumbura
            * `Africa/Cairo` - Africa/Cairo
            * `Africa/Casablanca` - Africa/Casablanca
            * `Africa/Ceuta` - Africa/Ceuta
            * `Africa/Conakry` - Africa/Conakry
            * `Africa/Dakar` - Africa/Dakar
            * `Africa/Dar_es_Salaam` - Africa/Dar_es_Salaam
            * `Africa/Djibouti` - Africa/Djibouti
            * `Africa/Douala` - Africa/Douala
            * `Africa/El_Aaiun` - Africa/El_Aaiun
            * `Africa/Freetown` - Africa/Freetown
            * `Africa/Gaborone` - Africa/Gaborone
            * `Africa/Harare` - Africa/Harare
            * `Africa/Johannesburg` - Africa/Johannesburg
            * `Africa/Juba` - Africa/Juba
            * `Africa/Kampala` - Africa/Kampala
            * `Africa/Khartoum` - Africa/Khartoum
            * `Africa/Kigali` - Africa/Kigali
            * `Africa/Kinshasa` - Africa/Kinshasa
            * `Africa/Lagos` - Africa/Lagos
            * `Africa/Libreville` - Africa/Libreville
            * `Africa/Lome` - Africa/Lome
            * `Africa/Luanda` - Africa/Luanda
            * `Africa/Lubumbashi` - Africa/Lubumbashi
            * `Africa/Lusaka` - Africa/Lusaka
            * `Africa/Malabo` - Africa/Malabo
            * `Africa/Maputo` - Africa/Maputo
            * `Africa/Maseru` - Africa/Maseru
            * `Africa/Mbabane` - Africa/Mbabane
            * `Africa/Mogadishu` - Africa/Mogadishu
            * `Africa/Monrovia` - Africa/Monrovia
            * `Africa/Nairobi` - Africa/Nairobi
            * `Africa/Ndjamena` - Africa/Ndjamena
            * `Africa/Niamey` - Africa/Niamey
            * `Africa/Nouakchott` - Africa/Nouakchott
            * `Africa/Ouagadougou` - Africa/Ouagadougou
            * `Africa/Porto-Novo` - Africa/Porto-Novo
            * `Africa/Sao_Tome` - Africa/Sao_Tome
            * `Africa/Timbuktu` - Africa/Timbuktu
            * `Africa/Tripoli` - Africa/Tripoli
            * `Africa/Tunis` - Africa/Tunis
            * `Africa/Windhoek` - Africa/Windhoek
            * `America/Adak` - America/Adak
            * `America/Anchorage` - America/Anchorage
            * `America/Anguilla` - America/Anguilla
            * `America/Antigua` - America/Antigua
            * `America/Araguaina` - America/Araguaina
            * `America/Argentina/Buenos_Aires` - America/Argentina/Buenos_Aires
            * `America/Argentina/Catamarca` - America/Argentina/Catamarca
            * `America/Argentina/ComodRivadavia` - America/Argentina/ComodRivadavia
            * `America/Argentina/Cordoba` - America/Argentina/Cordoba
            * `America/Argentina/Jujuy` - America/Argentina/Jujuy
            * `America/Argentina/La_Rioja` - America/Argentina/La_Rioja
            * `America/Argentina/Mendoza` - America/Argentina/Mendoza
            * `America/Argentina/Rio_Gallegos` - America/Argentina/Rio_Gallegos
            * `America/Argentina/Salta` - America/Argentina/Salta
            * `America/Argentina/San_Juan` - America/Argentina/San_Juan
            * `America/Argentina/San_Luis` - America/Argentina/San_Luis
            * `America/Argentina/Tucuman` - America/Argentina/Tucuman
            * `America/Argentina/Ushuaia` - America/Argentina/Ushuaia
            * `America/Aruba` - America/Aruba
            * `America/Asuncion` - America/Asuncion
            * `America/Atikokan` - America/Atikokan
            * `America/Atka` - America/Atka
            * `America/Bahia` - America/Bahia
            * `America/Bahia_Banderas` - America/Bahia_Banderas
            * `America/Barbados` - America/Barbados
            * `America/Belem` - America/Belem
            * `America/Belize` - America/Belize
            * `America/Blanc-Sablon` - America/Blanc-Sablon
            * `America/Boa_Vista` - America/Boa_Vista
            * `America/Bogota` - America/Bogota
            * `America/Boise` - America/Boise
            * `America/Buenos_Aires` - America/Buenos_Aires
            * `America/Cambridge_Bay` - America/Cambridge_Bay
            * `America/Campo_Grande` - America/Campo_Grande
            * `America/Cancun` - America/Cancun
            * `America/Caracas` - America/Caracas
            * `America/Catamarca` - America/Catamarca
            * `America/Cayenne` - America/Cayenne
            * `America/Cayman` - America/Cayman
            * `America/Chicago` - America/Chicago
            * `America/Chihuahua` - America/Chihuahua
            * `America/Ciudad_Juarez` - America/Ciudad_Juarez
            * `America/Coral_Harbour` - America/Coral_Harbour
            * `America/Cordoba` - America/Cordoba
            * `America/Costa_Rica` - America/Costa_Rica
            * `America/Creston` - America/Creston
            * `America/Cuiaba` - America/Cuiaba
            * `America/Curacao` - America/Curacao
            * `America/Danmarkshavn` - America/Danmarkshavn
            * `America/Dawson` - America/Dawson
            * `America/Dawson_Creek` - America/Dawson_Creek
            * `America/Denver` - America/Denver
            * `America/Detroit` - America/Detroit
            * `America/Dominica` - America/Dominica
            * `America/Edmonton` - America/Edmonton
            * `America/Eirunepe` - America/Eirunepe
            * `America/El_Salvador` - America/El_Salvador
            * `America/Ensenada` - America/Ensenada
            * `America/Fort_Nelson` - America/Fort_Nelson
            * `America/Fort_Wayne` - America/Fort_Wayne
            * `America/Fortaleza` - America/Fortaleza
            * `America/Glace_Bay` - America/Glace_Bay
            * `America/Godthab` - America/Godthab
            * `America/Goose_Bay` - America/Goose_Bay
            * `America/Grand_Turk` - America/Grand_Turk
            * `America/Grenada` - America/Grenada
            * `America/Guadeloupe` - America/Guadeloupe
            * `America/Guatemala` - America/Guatemala
            * `America/Guayaquil` - America/Guayaquil
            * `America/Guyana` - America/Guyana
            * `America/Halifax` - America/Halifax
            * `America/Havana` - America/Havana
            * `America/Hermosillo` - America/Hermosillo
            * `America/Indiana/Indianapolis` - America/Indiana/Indianapolis
            * `America/Indiana/Knox` - America/Indiana/Knox
            * `America/Indiana/Marengo` - America/Indiana/Marengo
            * `America/Indiana/Petersburg` - America/Indiana/Petersburg
            * `America/Indiana/Tell_City` - America/Indiana/Tell_City
            * `America/Indiana/Vevay` - America/Indiana/Vevay
            * `America/Indiana/Vincennes` - America/Indiana/Vincennes
            * `America/Indiana/Winamac` - America/Indiana/Winamac
            * `America/Indianapolis` - America/Indianapolis
            * `America/Inuvik` - America/Inuvik
            * `America/Iqaluit` - America/Iqaluit
            * `America/Jamaica` - America/Jamaica
            * `America/Jujuy` - America/Jujuy
            * `America/Juneau` - America/Juneau
            * `America/Kentucky/Louisville` - America/Kentucky/Louisville
            * `America/Kentucky/Monticello` - America/Kentucky/Monticello
            * `America/Knox_IN` - America/Knox_IN
            * `America/Kralendijk` - America/Kralendijk
            * `America/La_Paz` - America/La_Paz
            * `America/Lima` - America/Lima
            * `America/Los_Angeles` - America/Los_Angeles
            * `America/Louisville` - America/Louisville
            * `America/Lower_Princes` - America/Lower_Princes
            * `America/Maceio` - America/Maceio
            * `America/Managua` - America/Managua
            * `America/Manaus` - America/Manaus
            * `America/Marigot` - America/Marigot
            * `America/Martinique` - America/Martinique
            * `America/Matamoros` - America/Matamoros
            * `America/Mazatlan` - America/Mazatlan
            * `America/Mendoza` - America/Mendoza
            * `America/Menominee` - America/Menominee
            * `America/Merida` - America/Merida
            * `America/Metlakatla` - America/Metlakatla
            * `America/Mexico_City` - America/Mexico_City
            * `America/Miquelon` - America/Miquelon
            * `America/Moncton` - America/Moncton
            * `America/Monterrey` - America/Monterrey
            * `America/Montevideo` - America/Montevideo
            * `America/Montreal` - America/Montreal
            * `America/Montserrat` - America/Montserrat
            * `America/Nassau` - America/Nassau
            * `America/New_York` - America/New_York
            * `America/Nipigon` - America/Nipigon
            * `America/Nome` - America/Nome
            * `America/Noronha` - America/Noronha
            * `America/North_Dakota/Beulah` - America/North_Dakota/Beulah
            * `America/North_Dakota/Center` - America/North_Dakota/Center
            * `America/North_Dakota/New_Salem` - America/North_Dakota/New_Salem
            * `America/Nuuk` - America/Nuuk
            * `America/Ojinaga` - America/Ojinaga
            * `America/Panama` - America/Panama
            * `America/Pangnirtung` - America/Pangnirtung
            * `America/Paramaribo` - America/Paramaribo
            * `America/Phoenix` - America/Phoenix
            * `America/Port-au-Prince` - America/Port-au-Prince
            * `America/Port_of_Spain` - America/Port_of_Spain
            * `America/Porto_Acre` - America/Porto_Acre
            * `America/Porto_Velho` - America/Porto_Velho
            * `America/Puerto_Rico` - America/Puerto_Rico
            * `America/Punta_Arenas` - America/Punta_Arenas
            * `America/Rainy_River` - America/Rainy_River
            * `America/Rankin_Inlet` - America/Rankin_Inlet
            * `America/Recife` - America/Recife
            * `America/Regina` - America/Regina
            * `America/Resolute` - America/Resolute
            * `America/Rio_Branco` - America/Rio_Branco
            * `America/Rosario` - America/Rosario
            * `America/Santa_Isabel` - America/Santa_Isabel
            * `America/Santarem` - America/Santarem
            * `America/Santiago` - America/Santiago
            * `America/Santo_Domingo` - America/Santo_Domingo
            * `America/Sao_Paulo` - America/Sao_Paulo
            * `America/Scoresbysund` - America/Scoresbysund
            * `America/Shiprock` - America/Shiprock
            * `America/Sitka` - America/Sitka
            * `America/St_Barthelemy` - America/St_Barthelemy
            * `America/St_Johns` - America/St_Johns
            * `America/St_Kitts` - America/St_Kitts
            * `America/St_Lucia` - America/St_Lucia
            * `America/St_Thomas` - America/St_Thomas
            * `America/St_Vincent` - America/St_Vincent
            * `America/Swift_Current` - America/Swift_Current
            * `America/Tegucigalpa` - America/Tegucigalpa
            * `America/Thule` - America/Thule
            * `America/Thunder_Bay` - America/Thunder_Bay
            * `America/Tijuana` - America/Tijuana
            * `America/Toronto` - America/Toronto
            * `America/Tortola` - America/Tortola
            * `America/Vancouver` - America/Vancouver
            * `America/Virgin` - America/Virgin
            * `America/Whitehorse` - America/Whitehorse
            * `America/Winnipeg` - America/Winnipeg
            * `America/Yakutat` - America/Yakutat
            * `America/Yellowknife` - America/Yellowknife
            * `Antarctica/Casey` - Antarctica/Casey
            * `Antarctica/Davis` - Antarctica/Davis
            * `Antarctica/DumontDUrville` - Antarctica/DumontDUrville
            * `Antarctica/Macquarie` - Antarctica/Macquarie
            * `Antarctica/Mawson` - Antarctica/Mawson
            * `Antarctica/McMurdo` - Antarctica/McMurdo
            * `Antarctica/Palmer` - Antarctica/Palmer
            * `Antarctica/Rothera` - Antarctica/Rothera
            * `Antarctica/South_Pole` - Antarctica/South_Pole
            * `Antarctica/Syowa` - Antarctica/Syowa
            * `Antarctica/Troll` - Antarctica/Troll
            * `Antarctica/Vostok` - Antarctica/Vostok
            * `Arctic/Longyearbyen` - Arctic/Longyearbyen
            * `Asia/Aden` - Asia/Aden
            * `Asia/Almaty` - Asia/Almaty
            * `Asia/Amman` - Asia/Amman
            * `Asia/Anadyr` - Asia/Anadyr
            * `Asia/Aqtau` - Asia/Aqtau
            * `Asia/Aqtobe` - Asia/Aqtobe
            * `Asia/Ashgabat` - Asia/Ashgabat
            * `Asia/Ashkhabad` - Asia/Ashkhabad
            * `Asia/Atyrau` - Asia/Atyrau
            * `Asia/Baghdad` - Asia/Baghdad
            * `Asia/Bahrain` - Asia/Bahrain
            * `Asia/Baku` - Asia/Baku
            * `Asia/Bangkok` - Asia/Bangkok
            * `Asia/Barnaul` - Asia/Barnaul
            * `Asia/Beirut` - Asia/Beirut
            * `Asia/Bishkek` - Asia/Bishkek
            * `Asia/Brunei` - Asia/Brunei
            * `Asia/Calcutta` - Asia/Calcutta
            * `Asia/Chita` - Asia/Chita
            * `Asia/Choibalsan` - Asia/Choibalsan
            * `Asia/Chongqing` - Asia/Chongqing
            * `Asia/Chungking` - Asia/Chungking
            * `Asia/Colombo` - Asia/Colombo
            * `Asia/Dacca` - Asia/Dacca
            * `Asia/Damascus` - Asia/Damascus
            * `Asia/Dhaka` - Asia/Dhaka
            * `Asia/Dili` - Asia/Dili
            * `Asia/Dubai` - Asia/Dubai
            * `Asia/Dushanbe` - Asia/Dushanbe
            * `Asia/Famagusta` - Asia/Famagusta
            * `Asia/Gaza` - Asia/Gaza
            * `Asia/Harbin` - Asia/Harbin
            * `Asia/Hebron` - Asia/Hebron
            * `Asia/Ho_Chi_Minh` - Asia/Ho_Chi_Minh
            * `Asia/Hong_Kong` - Asia/Hong_Kong
            * `Asia/Hovd` - Asia/Hovd
            * `Asia/Irkutsk` - Asia/Irkutsk
            * `Asia/Istanbul` - Asia/Istanbul
            * `Asia/Jakarta` - Asia/Jakarta
            * `Asia/Jayapura` - Asia/Jayapura
            * `Asia/Jerusalem` - Asia/Jerusalem
            * `Asia/Kabul` - Asia/Kabul
            * `Asia/Kamchatka` - Asia/Kamchatka
            * `Asia/Karachi` - Asia/Karachi
            * `Asia/Kashgar` - Asia/Kashgar
            * `Asia/Kathmandu` - Asia/Kathmandu
            * `Asia/Katmandu` - Asia/Katmandu
            * `Asia/Khandyga` - Asia/Khandyga
            * `Asia/Kolkata` - Asia/Kolkata
            * `Asia/Krasnoyarsk` - Asia/Krasnoyarsk
            * `Asia/Kuala_Lumpur` - Asia/Kuala_Lumpur
            * `Asia/Kuching` - Asia/Kuching
            * `Asia/Kuwait` - Asia/Kuwait
            * `Asia/Macao` - Asia/Macao
            * `Asia/Macau` - Asia/Macau
            * `Asia/Magadan` - Asia/Magadan
            * `Asia/Makassar` - Asia/Makassar
            * `Asia/Manila` - Asia/Manila
            * `Asia/Muscat` - Asia/Muscat
            * `Asia/Nicosia` - Asia/Nicosia
            * `Asia/Novokuznetsk` - Asia/Novokuznetsk
            * `Asia/Novosibirsk` - Asia/Novosibirsk
            * `Asia/Omsk` - Asia/Omsk
            * `Asia/Oral` - Asia/Oral
            * `Asia/Phnom_Penh` - Asia/Phnom_Penh
            * `Asia/Pontianak` - Asia/Pontianak
            * `Asia/Pyongyang` - Asia/Pyongyang
            * `Asia/Qatar` - Asia/Qatar
            * `Asia/Qostanay` - Asia/Qostanay
            * `Asia/Qyzylorda` - Asia/Qyzylorda
            * `Asia/Rangoon` - Asia/Rangoon
            * `Asia/Riyadh` - Asia/Riyadh
            * `Asia/Saigon` - Asia/Saigon
            * `Asia/Sakhalin` - Asia/Sakhalin
            * `Asia/Samarkand` - Asia/Samarkand
            * `Asia/Seoul` - Asia/Seoul
            * `Asia/Shanghai` - Asia/Shanghai
            * `Asia/Singapore` - Asia/Singapore
            * `Asia/Srednekolymsk` - Asia/Srednekolymsk
            * `Asia/Taipei` - Asia/Taipei
            * `Asia/Tashkent` - Asia/Tashkent
            * `Asia/Tbilisi` - Asia/Tbilisi
            * `Asia/Tehran` - Asia/Tehran
            * `Asia/Tel_Aviv` - Asia/Tel_Aviv
            * `Asia/Thimbu` - Asia/Thimbu
            * `Asia/Thimphu` - Asia/Thimphu
            * `Asia/Tokyo` - Asia/Tokyo
            * `Asia/Tomsk` - Asia/Tomsk
            * `Asia/Ujung_Pandang` - Asia/Ujung_Pandang
            * `Asia/Ulaanbaatar` - Asia/Ulaanbaatar
            * `Asia/Ulan_Bator` - Asia/Ulan_Bator
            * `Asia/Urumqi` - Asia/Urumqi
            * `Asia/Ust-Nera` - Asia/Ust-Nera
            * `Asia/Vientiane` - Asia/Vientiane
            * `Asia/Vladivostok` - Asia/Vladivostok
            * `Asia/Yakutsk` - Asia/Yakutsk
            * `Asia/Yangon` - Asia/Yangon
            * `Asia/Yekaterinburg` - Asia/Yekaterinburg
            * `Asia/Yerevan` - Asia/Yerevan
            * `Atlantic/Azores` - Atlantic/Azores
            * `Atlantic/Bermuda` - Atlantic/Bermuda
            * `Atlantic/Canary` - Atlantic/Canary
            * `Atlantic/Cape_Verde` - Atlantic/Cape_Verde
            * `Atlantic/Faeroe` - Atlantic/Faeroe
            * `Atlantic/Faroe` - Atlantic/Faroe
            * `Atlantic/Jan_Mayen` - Atlantic/Jan_Mayen
            * `Atlantic/Madeira` - Atlantic/Madeira
            * `Atlantic/Reykjavik` - Atlantic/Reykjavik
            * `Atlantic/South_Georgia` - Atlantic/South_Georgia
            * `Atlantic/St_Helena` - Atlantic/St_Helena
            * `Atlantic/Stanley` - Atlantic/Stanley
            * `Australia/ACT` - Australia/ACT
            * `Australia/Adelaide` - Australia/Adelaide
            * `Australia/Brisbane` - Australia/Brisbane
            * `Australia/Broken_Hill` - Australia/Broken_Hill
            * `Australia/Canberra` - Australia/Canberra
            * `Australia/Currie` - Australia/Currie
            * `Australia/Darwin` - Australia/Darwin
            * `Australia/Eucla` - Australia/Eucla
            * `Australia/Hobart` - Australia/Hobart
            * `Australia/LHI` - Australia/LHI
            * `Australia/Lindeman` - Australia/Lindeman
            * `Australia/Lord_Howe` - Australia/Lord_Howe
            * `Australia/Melbourne` - Australia/Melbourne
            * `Australia/NSW` - Australia/NSW
            * `Australia/North` - Australia/North
            * `Australia/Perth` - Australia/Perth
            * `Australia/Queensland` - Australia/Queensland
            * `Australia/South` - Australia/South
            * `Australia/Sydney` - Australia/Sydney
            * `Australia/Tasmania` - Australia/Tasmania
            * `Australia/Victoria` - Australia/Victoria
            * `Australia/West` - Australia/West
            * `Australia/Yancowinna` - Australia/Yancowinna
            * `Brazil/Acre` - Brazil/Acre
            * `Brazil/DeNoronha` - Brazil/DeNoronha
            * `Brazil/East` - Brazil/East
            * `Brazil/West` - Brazil/West
            * `CET` - CET
            * `CST6CDT` - CST6CDT
            * `Canada/Atlantic` - Canada/Atlantic
            * `Canada/Central` - Canada/Central
            * `Canada/Eastern` - Canada/Eastern
            * `Canada/Mountain` - Canada/Mountain
            * `Canada/Newfoundland` - Canada/Newfoundland
            * `Canada/Pacific` - Canada/Pacific
            * `Canada/Saskatchewan` - Canada/Saskatchewan
            * `Canada/Yukon` - Canada/Yukon
            * `Chile/Continental` - Chile/Continental
            * `Chile/EasterIsland` - Chile/EasterIsland
            * `Cuba` - Cuba
            * `EET` - EET
            * `EST` - EST
            * `EST5EDT` - EST5EDT
            * `Egypt` - Egypt
            * `Eire` - Eire
            * `Etc/GMT` - Etc/GMT
            * `Etc/GMT+0` - Etc/GMT+0
            * `Etc/GMT+1` - Etc/GMT+1
            * `Etc/GMT+10` - Etc/GMT+10
            * `Etc/GMT+11` - Etc/GMT+11
            * `Etc/GMT+12` - Etc/GMT+12
            * `Etc/GMT+2` - Etc/GMT+2
            * `Etc/GMT+3` - Etc/GMT+3
            * `Etc/GMT+4` - Etc/GMT+4
            * `Etc/GMT+5` - Etc/GMT+5
            * `Etc/GMT+6` - Etc/GMT+6
            * `Etc/GMT+7` - Etc/GMT+7
            * `Etc/GMT+8` - Etc/GMT+8
            * `Etc/GMT+9` - Etc/GMT+9
            * `Etc/GMT-0` - Etc/GMT-0
            * `Etc/GMT-1` - Etc/GMT-1
            * `Etc/GMT-10` - Etc/GMT-10
            * `Etc/GMT-11` - Etc/GMT-11
            * `Etc/GMT-12` - Etc/GMT-12
            * `Etc/GMT-13` - Etc/GMT-13
            * `Etc/GMT-14` - Etc/GMT-14
            * `Etc/GMT-2` - Etc/GMT-2
            * `Etc/GMT-3` - Etc/GMT-3
            * `Etc/GMT-4` - Etc/GMT-4
            * `Etc/GMT-5` - Etc/GMT-5
            * `Etc/GMT-6` - Etc/GMT-6
            * `Etc/GMT-7` - Etc/GMT-7
            * `Etc/GMT-8` - Etc/GMT-8
            * `Etc/GMT-9` - Etc/GMT-9
            * `Etc/GMT0` - Etc/GMT0
            * `Etc/Greenwich` - Etc/Greenwich
            * `Etc/UCT` - Etc/UCT
            * `Etc/UTC` - Etc/UTC
            * `Etc/Universal` - Etc/Universal
            * `Etc/Zulu` - Etc/Zulu
            * `Europe/Amsterdam` - Europe/Amsterdam
            * `Europe/Andorra` - Europe/Andorra
            * `Europe/Astrakhan` - Europe/Astrakhan
            * `Europe/Athens` - Europe/Athens
            * `Europe/Belfast` - Europe/Belfast
            * `Europe/Belgrade` - Europe/Belgrade
            * `Europe/Berlin` - Europe/Berlin
            * `Europe/Bratislava` - Europe/Bratislava
            * `Europe/Brussels` - Europe/Brussels
            * `Europe/Bucharest` - Europe/Bucharest
            * `Europe/Budapest` - Europe/Budapest
            * `Europe/Busingen` - Europe/Busingen
            * `Europe/Chisinau` - Europe/Chisinau
            * `Europe/Copenhagen` - Europe/Copenhagen
            * `Europe/Dublin` - Europe/Dublin
            * `Europe/Gibraltar` - Europe/Gibraltar
            * `Europe/Guernsey` - Europe/Guernsey
            * `Europe/Helsinki` - Europe/Helsinki
            * `Europe/Isle_of_Man` - Europe/Isle_of_Man
            * `Europe/Istanbul` - Europe/Istanbul
            * `Europe/Jersey` - Europe/Jersey
            * `Europe/Kaliningrad` - Europe/Kaliningrad
            * `Europe/Kiev` - Europe/Kiev
            * `Europe/Kirov` - Europe/Kirov
            * `Europe/Kyiv` - Europe/Kyiv
            * `Europe/Lisbon` - Europe/Lisbon
            * `Europe/Ljubljana` - Europe/Ljubljana
            * `Europe/London` - Europe/London
            * `Europe/Luxembourg` - Europe/Luxembourg
            * `Europe/Madrid` - Europe/Madrid
            * `Europe/Malta` - Europe/Malta
            * `Europe/Mariehamn` - Europe/Mariehamn
            * `Europe/Minsk` - Europe/Minsk
            * `Europe/Monaco` - Europe/Monaco
            * `Europe/Moscow` - Europe/Moscow
            * `Europe/Nicosia` - Europe/Nicosia
            * `Europe/Oslo` - Europe/Oslo
            * `Europe/Paris` - Europe/Paris
            * `Europe/Podgorica` - Europe/Podgorica
            * `Europe/Prague` - Europe/Prague
            * `Europe/Riga` - Europe/Riga
            * `Europe/Rome` - Europe/Rome
            * `Europe/Samara` - Europe/Samara
            * `Europe/San_Marino` - Europe/San_Marino
            * `Europe/Sarajevo` - Europe/Sarajevo
            * `Europe/Saratov` - Europe/Saratov
            * `Europe/Simferopol` - Europe/Simferopol
            * `Europe/Skopje` - Europe/Skopje
            * `Europe/Sofia` - Europe/Sofia
            * `Europe/Stockholm` - Europe/Stockholm
            * `Europe/Tallinn` - Europe/Tallinn
            * `Europe/Tirane` - Europe/Tirane
            * `Europe/Tiraspol` - Europe/Tiraspol
            * `Europe/Ulyanovsk` - Europe/Ulyanovsk
            * `Europe/Uzhgorod` - Europe/Uzhgorod
            * `Europe/Vaduz` - Europe/Vaduz
            * `Europe/Vatican` - Europe/Vatican
            * `Europe/Vienna` - Europe/Vienna
            * `Europe/Vilnius` - Europe/Vilnius
            * `Europe/Volgograd` - Europe/Volgograd
            * `Europe/Warsaw` - Europe/Warsaw
            * `Europe/Zagreb` - Europe/Zagreb
            * `Europe/Zaporozhye` - Europe/Zaporozhye
            * `Europe/Zurich` - Europe/Zurich
            * `GB` - GB
            * `GB-Eire` - GB-Eire
            * `GMT` - GMT
            * `GMT+0` - GMT+0
            * `GMT-0` - GMT-0
            * `GMT0` - GMT0
            * `Greenwich` - Greenwich
            * `HST` - HST
            * `Hongkong` - Hongkong
            * `Iceland` - Iceland
            * `Indian/Antananarivo` - Indian/Antananarivo
            * `Indian/Chagos` - Indian/Chagos
            * `Indian/Christmas` - Indian/Christmas
            * `Indian/Cocos` - Indian/Cocos
            * `Indian/Comoro` - Indian/Comoro
            * `Indian/Kerguelen` - Indian/Kerguelen
            * `Indian/Mahe` - Indian/Mahe
            * `Indian/Maldives` - Indian/Maldives
            * `Indian/Mauritius` - Indian/Mauritius
            * `Indian/Mayotte` - Indian/Mayotte
            * `Indian/Reunion` - Indian/Reunion
            * `Iran` - Iran
            * `Israel` - Israel
            * `Jamaica` - Jamaica
            * `Japan` - Japan
            * `Kwajalein` - Kwajalein
            * `Libya` - Libya
            * `MET` - MET
            * `MST` - MST
            * `MST7MDT` - MST7MDT
            * `Mexico/BajaNorte` - Mexico/BajaNorte
            * `Mexico/BajaSur` - Mexico/BajaSur
            * `Mexico/General` - Mexico/General
            * `NZ` - NZ
            * `NZ-CHAT` - NZ-CHAT
            * `Navajo` - Navajo
            * `PRC` - PRC
            * `PST8PDT` - PST8PDT
            * `Pacific/Apia` - Pacific/Apia
            * `Pacific/Auckland` - Pacific/Auckland
            * `Pacific/Bougainville` - Pacific/Bougainville
            * `Pacific/Chatham` - Pacific/Chatham
            * `Pacific/Chuuk` - Pacific/Chuuk
            * `Pacific/Easter` - Pacific/Easter
            * `Pacific/Efate` - Pacific/Efate
            * `Pacific/Enderbury` - Pacific/Enderbury
            * `Pacific/Fakaofo` - Pacific/Fakaofo
            * `Pacific/Fiji` - Pacific/Fiji
            * `Pacific/Funafuti` - Pacific/Funafuti
            * `Pacific/Galapagos` - Pacific/Galapagos
            * `Pacific/Gambier` - Pacific/Gambier
            * `Pacific/Guadalcanal` - Pacific/Guadalcanal
            * `Pacific/Guam` - Pacific/Guam
            * `Pacific/Honolulu` - Pacific/Honolulu
            * `Pacific/Johnston` - Pacific/Johnston
            * `Pacific/Kanton` - Pacific/Kanton
            * `Pacific/Kiritimati` - Pacific/Kiritimati
            * `Pacific/Kosrae` - Pacific/Kosrae
            * `Pacific/Kwajalein` - Pacific/Kwajalein
            * `Pacific/Majuro` - Pacific/Majuro
            * `Pacific/Marquesas` - Pacific/Marquesas
            * `Pacific/Midway` - Pacific/Midway
            * `Pacific/Nauru` - Pacific/Nauru
            * `Pacific/Niue` - Pacific/Niue
            * `Pacific/Norfolk` - Pacific/Norfolk
            * `Pacific/Noumea` - Pacific/Noumea
            * `Pacific/Pago_Pago` - Pacific/Pago_Pago
            * `Pacific/Palau` - Pacific/Palau
            * `Pacific/Pitcairn` - Pacific/Pitcairn
            * `Pacific/Pohnpei` - Pacific/Pohnpei
            * `Pacific/Ponape` - Pacific/Ponape
            * `Pacific/Port_Moresby` - Pacific/Port_Moresby
            * `Pacific/Rarotonga` - Pacific/Rarotonga
            * `Pacific/Saipan` - Pacific/Saipan
            * `Pacific/Samoa` - Pacific/Samoa
            * `Pacific/Tahiti` - Pacific/Tahiti
            * `Pacific/Tarawa` - Pacific/Tarawa
            * `Pacific/Tongatapu` - Pacific/Tongatapu
            * `Pacific/Truk` - Pacific/Truk
            * `Pacific/Wake` - Pacific/Wake
            * `Pacific/Wallis` - Pacific/Wallis
            * `Pacific/Yap` - Pacific/Yap
            * `Poland` - Poland
            * `Portugal` - Portugal
            * `ROC` - ROC
            * `ROK` - ROK
            * `Singapore` - Singapore
            * `Turkey` - Turkey
            * `UCT` - UCT
            * `US/Alaska` - US/Alaska
            * `US/Aleutian` - US/Aleutian
            * `US/Arizona` - US/Arizona
            * `US/Central` - US/Central
            * `US/East-Indiana` - US/East-Indiana
            * `US/Eastern` - US/Eastern
            * `US/Hawaii` - US/Hawaii
            * `US/Indiana-Starke` - US/Indiana-Starke
            * `US/Michigan` - US/Michigan
            * `US/Mountain` - US/Mountain
            * `US/Pacific` - US/Pacific
            * `US/Samoa` - US/Samoa
            * `UTC` - UTC
            * `Universal` - Universal
            * `W-SU` - W-SU
            * `WET` - WET
            * `Zulu` - Zulu
        enable_product_grade (Union[Unset, bool]): Displays a grade letter next to a product to show the overall health.
        product_grade (Union[Unset, str]):
        product_grade_a (Union[Unset, int]): Percentage score for an 'A' >=
        product_grade_b (Union[Unset, int]): Percentage score for a 'B' >=
        product_grade_c (Union[Unset, int]): Percentage score for a 'C' >=
        product_grade_d (Union[Unset, int]): Percentage score for a 'D' >=
        product_grade_f (Union[Unset, int]): Percentage score for an 'F' <=
        enable_product_tag_inheritance (Union[Unset, bool]): Enables product tag inheritance globally for all products.
            Any tags added on a product will automatically be added to all Engagements, Tests, and Findings
        enable_benchmark (Union[Unset, bool]): Enables Benchmarks such as the OWASP ASVS (Application Security
            Verification Standard)
        enable_template_match (Union[Unset, bool]): Enables global remediation advice and matching on CWE and Title. The
            text will be replaced for mitigation, impact and references on a finding. Useful for providing consistent impact
            and remediation advice regardless of the scanner.
        engagement_auto_close (Union[Unset, bool]): Closes an engagement after 3 days (default) past due date including
            last update.
        engagement_auto_close_days (Union[Unset, int]): Closes an engagement after the specified number of days past due
            date including last update.
        enable_finding_sla (Union[Unset, bool]): Enables Finding SLA's for time to remediate.
        enable_notify_sla_active (Union[Unset, bool]): Enables Notify when time to remediate according to Finding SLA's
            is breached for active Findings.
        enable_notify_sla_active_verified (Union[Unset, bool]): Enables Notify when time to remediate according to
            Finding SLA's is breached for active, verified Findings.
        enable_notify_sla_jira_only (Union[Unset, bool]): Enables Notify when time to remediate according to Finding
            SLA's is breached for Findings that are linked to JIRA issues. Notification is disabled for Findings not linked
            to JIRA issues
        enable_notify_sla_exponential_backoff (Union[Unset, bool]): Enable an exponential backoff strategy for SLA
            breach notifications, e.g. 1, 2, 4, 8, etc. Otherwise it alerts every day
        allow_anonymous_survey_repsonse (Union[Unset, bool]): Enable anyone with a link to the survey to answer a survey
        credentials (Union[Unset, str]):
        disclaimer (Union[Unset, str]): Include this custom disclaimer on all notifications and generated reports
        risk_acceptance_form_default_days (Union[Unset, None, int]): Default expiry period for risk acceptance form.
        risk_acceptance_notify_before_expiration (Union[Unset, None, int]): Notify X days before risk acceptance
            expires. Leave empty to disable.
        enable_credentials (Union[Unset, bool]): With this setting turned off, credentials will be disabled in the user
            interface.
        enable_questionnaires (Union[Unset, bool]): With this setting turned off, questionnaires will be disabled in the
            user interface.
        enable_checklists (Union[Unset, bool]): With this setting turned off, checklists will be disabled in the user
            interface.
        enable_endpoint_metadata_import (Union[Unset, bool]): With this setting turned off, endpoint metadata import
            will be disabled in the user interface.
        enable_user_profile_editable (Union[Unset, bool]): When turned on users can edit their profiles
        enable_product_tracking_files (Union[Unset, bool]): With this setting turned off, the product tracking files
            will be disabled in the user interface.
        enable_finding_groups (Union[Unset, bool]): With this setting turned off, the Finding Groups will be disabled.
        enable_calendar (Union[Unset, bool]): With this setting turned off, the Calendar will be disabled in the user
            interface.
        default_group_email_pattern (Union[Unset, str]): New users will only be assigned to the default group, when
            their email address matches this regex pattern. This is optional condition.
        minimum_password_length (Union[Unset, int]): Requires user to set passwords greater than minimum length.
        maximum_password_length (Union[Unset, int]): Requires user to set passwords less than maximum length.
        number_character_required (Union[Unset, bool]): Requires user passwords to contain at least one digit (0-9).
        special_character_required (Union[Unset, bool]): Requires user passwords to contain at least one special
            character (()[]{}|\`~!@#$%^&*_-+=;:'",<>./?).
        lowercase_character_required (Union[Unset, bool]): Requires user passwords to contain at least one lowercase
            letter (a-z).
        uppercase_character_required (Union[Unset, bool]): Requires user passwords to contain at least one uppercase
            letter (A-Z).
        non_common_password_required (Union[Unset, bool]): Requires user passwords to not be part of list of common
            passwords.
        default_group (Union[Unset, None, int]): New users will be assigned to this group.
        default_group_role (Union[Unset, None, int]): New users will be assigned to their default group with this role.
    """

    enable_auditlog: Union[Unset, bool] = UNSET
    enable_deduplication: Union[Unset, bool] = UNSET
    delete_duplicates: Union[Unset, bool] = UNSET
    max_dupes: Union[Unset, None, int] = UNSET
    email_from: Union[Unset, str] = UNSET
    enable_jira: Union[Unset, bool] = UNSET
    enable_jira_web_hook: Union[Unset, bool] = UNSET
    disable_jira_webhook_secret: Union[Unset, bool] = UNSET
    jira_webhook_secret: Union[Unset, None, str] = UNSET
    jira_minimum_severity: Union[Unset, None, SystemSettingsRequestJiraMinimumSeverity] = UNSET
    jira_labels: Union[Unset, None, str] = UNSET
    add_vulnerability_id_to_jira_label: Union[Unset, bool] = UNSET
    enable_github: Union[Unset, bool] = UNSET
    enable_slack_notifications: Union[Unset, bool] = UNSET
    slack_channel: Union[Unset, str] = UNSET
    slack_token: Union[Unset, str] = UNSET
    slack_username: Union[Unset, str] = UNSET
    enable_msteams_notifications: Union[Unset, bool] = UNSET
    msteams_url: Union[Unset, str] = UNSET
    enable_mail_notifications: Union[Unset, bool] = UNSET
    mail_notifications_to: Union[Unset, str] = UNSET
    false_positive_history: Union[Unset, bool] = UNSET
    retroactive_false_positive_history: Union[Unset, bool] = UNSET
    url_prefix: Union[Unset, str] = UNSET
    team_name: Union[Unset, str] = UNSET
    time_zone: Union[Unset, SystemSettingsRequestTimeZone] = UNSET
    enable_product_grade: Union[Unset, bool] = UNSET
    product_grade: Union[Unset, str] = UNSET
    product_grade_a: Union[Unset, int] = UNSET
    product_grade_b: Union[Unset, int] = UNSET
    product_grade_c: Union[Unset, int] = UNSET
    product_grade_d: Union[Unset, int] = UNSET
    product_grade_f: Union[Unset, int] = UNSET
    enable_product_tag_inheritance: Union[Unset, bool] = UNSET
    enable_benchmark: Union[Unset, bool] = UNSET
    enable_template_match: Union[Unset, bool] = UNSET
    engagement_auto_close: Union[Unset, bool] = UNSET
    engagement_auto_close_days: Union[Unset, int] = UNSET
    enable_finding_sla: Union[Unset, bool] = UNSET
    enable_notify_sla_active: Union[Unset, bool] = UNSET
    enable_notify_sla_active_verified: Union[Unset, bool] = UNSET
    enable_notify_sla_jira_only: Union[Unset, bool] = UNSET
    enable_notify_sla_exponential_backoff: Union[Unset, bool] = UNSET
    allow_anonymous_survey_repsonse: Union[Unset, bool] = UNSET
    credentials: Union[Unset, str] = UNSET
    disclaimer: Union[Unset, str] = UNSET
    risk_acceptance_form_default_days: Union[Unset, None, int] = UNSET
    risk_acceptance_notify_before_expiration: Union[Unset, None, int] = UNSET
    enable_credentials: Union[Unset, bool] = UNSET
    enable_questionnaires: Union[Unset, bool] = UNSET
    enable_checklists: Union[Unset, bool] = UNSET
    enable_endpoint_metadata_import: Union[Unset, bool] = UNSET
    enable_user_profile_editable: Union[Unset, bool] = UNSET
    enable_product_tracking_files: Union[Unset, bool] = UNSET
    enable_finding_groups: Union[Unset, bool] = UNSET
    enable_calendar: Union[Unset, bool] = UNSET
    default_group_email_pattern: Union[Unset, str] = UNSET
    minimum_password_length: Union[Unset, int] = UNSET
    maximum_password_length: Union[Unset, int] = UNSET
    number_character_required: Union[Unset, bool] = UNSET
    special_character_required: Union[Unset, bool] = UNSET
    lowercase_character_required: Union[Unset, bool] = UNSET
    uppercase_character_required: Union[Unset, bool] = UNSET
    non_common_password_required: Union[Unset, bool] = UNSET
    default_group: Union[Unset, None, int] = UNSET
    default_group_role: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_auditlog = self.enable_auditlog
        enable_deduplication = self.enable_deduplication
        delete_duplicates = self.delete_duplicates
        max_dupes = self.max_dupes
        email_from = self.email_from
        enable_jira = self.enable_jira
        enable_jira_web_hook = self.enable_jira_web_hook
        disable_jira_webhook_secret = self.disable_jira_webhook_secret
        jira_webhook_secret = self.jira_webhook_secret
        jira_minimum_severity: Union[Unset, None, str] = UNSET
        if not isinstance(self.jira_minimum_severity, Unset):
            jira_minimum_severity = self.jira_minimum_severity.value if self.jira_minimum_severity else None

        jira_labels = self.jira_labels
        add_vulnerability_id_to_jira_label = self.add_vulnerability_id_to_jira_label
        enable_github = self.enable_github
        enable_slack_notifications = self.enable_slack_notifications
        slack_channel = self.slack_channel
        slack_token = self.slack_token
        slack_username = self.slack_username
        enable_msteams_notifications = self.enable_msteams_notifications
        msteams_url = self.msteams_url
        enable_mail_notifications = self.enable_mail_notifications
        mail_notifications_to = self.mail_notifications_to
        false_positive_history = self.false_positive_history
        retroactive_false_positive_history = self.retroactive_false_positive_history
        url_prefix = self.url_prefix
        team_name = self.team_name
        time_zone: Union[Unset, str] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.value

        enable_product_grade = self.enable_product_grade
        product_grade = self.product_grade
        product_grade_a = self.product_grade_a
        product_grade_b = self.product_grade_b
        product_grade_c = self.product_grade_c
        product_grade_d = self.product_grade_d
        product_grade_f = self.product_grade_f
        enable_product_tag_inheritance = self.enable_product_tag_inheritance
        enable_benchmark = self.enable_benchmark
        enable_template_match = self.enable_template_match
        engagement_auto_close = self.engagement_auto_close
        engagement_auto_close_days = self.engagement_auto_close_days
        enable_finding_sla = self.enable_finding_sla
        enable_notify_sla_active = self.enable_notify_sla_active
        enable_notify_sla_active_verified = self.enable_notify_sla_active_verified
        enable_notify_sla_jira_only = self.enable_notify_sla_jira_only
        enable_notify_sla_exponential_backoff = self.enable_notify_sla_exponential_backoff
        allow_anonymous_survey_repsonse = self.allow_anonymous_survey_repsonse
        credentials = self.credentials
        disclaimer = self.disclaimer
        risk_acceptance_form_default_days = self.risk_acceptance_form_default_days
        risk_acceptance_notify_before_expiration = self.risk_acceptance_notify_before_expiration
        enable_credentials = self.enable_credentials
        enable_questionnaires = self.enable_questionnaires
        enable_checklists = self.enable_checklists
        enable_endpoint_metadata_import = self.enable_endpoint_metadata_import
        enable_user_profile_editable = self.enable_user_profile_editable
        enable_product_tracking_files = self.enable_product_tracking_files
        enable_finding_groups = self.enable_finding_groups
        enable_calendar = self.enable_calendar
        default_group_email_pattern = self.default_group_email_pattern
        minimum_password_length = self.minimum_password_length
        maximum_password_length = self.maximum_password_length
        number_character_required = self.number_character_required
        special_character_required = self.special_character_required
        lowercase_character_required = self.lowercase_character_required
        uppercase_character_required = self.uppercase_character_required
        non_common_password_required = self.non_common_password_required
        default_group = self.default_group
        default_group_role = self.default_group_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_auditlog is not UNSET:
            field_dict["enable_auditlog"] = enable_auditlog
        if enable_deduplication is not UNSET:
            field_dict["enable_deduplication"] = enable_deduplication
        if delete_duplicates is not UNSET:
            field_dict["delete_duplicates"] = delete_duplicates
        if max_dupes is not UNSET:
            field_dict["max_dupes"] = max_dupes
        if email_from is not UNSET:
            field_dict["email_from"] = email_from
        if enable_jira is not UNSET:
            field_dict["enable_jira"] = enable_jira
        if enable_jira_web_hook is not UNSET:
            field_dict["enable_jira_web_hook"] = enable_jira_web_hook
        if disable_jira_webhook_secret is not UNSET:
            field_dict["disable_jira_webhook_secret"] = disable_jira_webhook_secret
        if jira_webhook_secret is not UNSET:
            field_dict["jira_webhook_secret"] = jira_webhook_secret
        if jira_minimum_severity is not UNSET:
            field_dict["jira_minimum_severity"] = jira_minimum_severity
        if jira_labels is not UNSET:
            field_dict["jira_labels"] = jira_labels
        if add_vulnerability_id_to_jira_label is not UNSET:
            field_dict["add_vulnerability_id_to_jira_label"] = add_vulnerability_id_to_jira_label
        if enable_github is not UNSET:
            field_dict["enable_github"] = enable_github
        if enable_slack_notifications is not UNSET:
            field_dict["enable_slack_notifications"] = enable_slack_notifications
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel
        if slack_token is not UNSET:
            field_dict["slack_token"] = slack_token
        if slack_username is not UNSET:
            field_dict["slack_username"] = slack_username
        if enable_msteams_notifications is not UNSET:
            field_dict["enable_msteams_notifications"] = enable_msteams_notifications
        if msteams_url is not UNSET:
            field_dict["msteams_url"] = msteams_url
        if enable_mail_notifications is not UNSET:
            field_dict["enable_mail_notifications"] = enable_mail_notifications
        if mail_notifications_to is not UNSET:
            field_dict["mail_notifications_to"] = mail_notifications_to
        if false_positive_history is not UNSET:
            field_dict["false_positive_history"] = false_positive_history
        if retroactive_false_positive_history is not UNSET:
            field_dict["retroactive_false_positive_history"] = retroactive_false_positive_history
        if url_prefix is not UNSET:
            field_dict["url_prefix"] = url_prefix
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if enable_product_grade is not UNSET:
            field_dict["enable_product_grade"] = enable_product_grade
        if product_grade is not UNSET:
            field_dict["product_grade"] = product_grade
        if product_grade_a is not UNSET:
            field_dict["product_grade_a"] = product_grade_a
        if product_grade_b is not UNSET:
            field_dict["product_grade_b"] = product_grade_b
        if product_grade_c is not UNSET:
            field_dict["product_grade_c"] = product_grade_c
        if product_grade_d is not UNSET:
            field_dict["product_grade_d"] = product_grade_d
        if product_grade_f is not UNSET:
            field_dict["product_grade_f"] = product_grade_f
        if enable_product_tag_inheritance is not UNSET:
            field_dict["enable_product_tag_inheritance"] = enable_product_tag_inheritance
        if enable_benchmark is not UNSET:
            field_dict["enable_benchmark"] = enable_benchmark
        if enable_template_match is not UNSET:
            field_dict["enable_template_match"] = enable_template_match
        if engagement_auto_close is not UNSET:
            field_dict["engagement_auto_close"] = engagement_auto_close
        if engagement_auto_close_days is not UNSET:
            field_dict["engagement_auto_close_days"] = engagement_auto_close_days
        if enable_finding_sla is not UNSET:
            field_dict["enable_finding_sla"] = enable_finding_sla
        if enable_notify_sla_active is not UNSET:
            field_dict["enable_notify_sla_active"] = enable_notify_sla_active
        if enable_notify_sla_active_verified is not UNSET:
            field_dict["enable_notify_sla_active_verified"] = enable_notify_sla_active_verified
        if enable_notify_sla_jira_only is not UNSET:
            field_dict["enable_notify_sla_jira_only"] = enable_notify_sla_jira_only
        if enable_notify_sla_exponential_backoff is not UNSET:
            field_dict["enable_notify_sla_exponential_backoff"] = enable_notify_sla_exponential_backoff
        if allow_anonymous_survey_repsonse is not UNSET:
            field_dict["allow_anonymous_survey_repsonse"] = allow_anonymous_survey_repsonse
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if disclaimer is not UNSET:
            field_dict["disclaimer"] = disclaimer
        if risk_acceptance_form_default_days is not UNSET:
            field_dict["risk_acceptance_form_default_days"] = risk_acceptance_form_default_days
        if risk_acceptance_notify_before_expiration is not UNSET:
            field_dict["risk_acceptance_notify_before_expiration"] = risk_acceptance_notify_before_expiration
        if enable_credentials is not UNSET:
            field_dict["enable_credentials"] = enable_credentials
        if enable_questionnaires is not UNSET:
            field_dict["enable_questionnaires"] = enable_questionnaires
        if enable_checklists is not UNSET:
            field_dict["enable_checklists"] = enable_checklists
        if enable_endpoint_metadata_import is not UNSET:
            field_dict["enable_endpoint_metadata_import"] = enable_endpoint_metadata_import
        if enable_user_profile_editable is not UNSET:
            field_dict["enable_user_profile_editable"] = enable_user_profile_editable
        if enable_product_tracking_files is not UNSET:
            field_dict["enable_product_tracking_files"] = enable_product_tracking_files
        if enable_finding_groups is not UNSET:
            field_dict["enable_finding_groups"] = enable_finding_groups
        if enable_calendar is not UNSET:
            field_dict["enable_calendar"] = enable_calendar
        if default_group_email_pattern is not UNSET:
            field_dict["default_group_email_pattern"] = default_group_email_pattern
        if minimum_password_length is not UNSET:
            field_dict["minimum_password_length"] = minimum_password_length
        if maximum_password_length is not UNSET:
            field_dict["maximum_password_length"] = maximum_password_length
        if number_character_required is not UNSET:
            field_dict["number_character_required"] = number_character_required
        if special_character_required is not UNSET:
            field_dict["special_character_required"] = special_character_required
        if lowercase_character_required is not UNSET:
            field_dict["lowercase_character_required"] = lowercase_character_required
        if uppercase_character_required is not UNSET:
            field_dict["uppercase_character_required"] = uppercase_character_required
        if non_common_password_required is not UNSET:
            field_dict["non_common_password_required"] = non_common_password_required
        if default_group is not UNSET:
            field_dict["default_group"] = default_group
        if default_group_role is not UNSET:
            field_dict["default_group_role"] = default_group_role

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        enable_auditlog = (
            self.enable_auditlog
            if isinstance(self.enable_auditlog, Unset)
            else (None, str(self.enable_auditlog).encode(), "text/plain")
        )
        enable_deduplication = (
            self.enable_deduplication
            if isinstance(self.enable_deduplication, Unset)
            else (None, str(self.enable_deduplication).encode(), "text/plain")
        )
        delete_duplicates = (
            self.delete_duplicates
            if isinstance(self.delete_duplicates, Unset)
            else (None, str(self.delete_duplicates).encode(), "text/plain")
        )
        max_dupes = (
            self.max_dupes if isinstance(self.max_dupes, Unset) else (None, str(self.max_dupes).encode(), "text/plain")
        )
        email_from = (
            self.email_from
            if isinstance(self.email_from, Unset)
            else (None, str(self.email_from).encode(), "text/plain")
        )
        enable_jira = (
            self.enable_jira
            if isinstance(self.enable_jira, Unset)
            else (None, str(self.enable_jira).encode(), "text/plain")
        )
        enable_jira_web_hook = (
            self.enable_jira_web_hook
            if isinstance(self.enable_jira_web_hook, Unset)
            else (None, str(self.enable_jira_web_hook).encode(), "text/plain")
        )
        disable_jira_webhook_secret = (
            self.disable_jira_webhook_secret
            if isinstance(self.disable_jira_webhook_secret, Unset)
            else (None, str(self.disable_jira_webhook_secret).encode(), "text/plain")
        )
        jira_webhook_secret = (
            self.jira_webhook_secret
            if isinstance(self.jira_webhook_secret, Unset)
            else (None, str(self.jira_webhook_secret).encode(), "text/plain")
        )
        jira_minimum_severity: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.jira_minimum_severity, Unset):
            jira_minimum_severity = (
                (None, str(self.jira_minimum_severity.value).encode(), "text/plain")
                if self.jira_minimum_severity
                else None
            )

        jira_labels = (
            self.jira_labels
            if isinstance(self.jira_labels, Unset)
            else (None, str(self.jira_labels).encode(), "text/plain")
        )
        add_vulnerability_id_to_jira_label = (
            self.add_vulnerability_id_to_jira_label
            if isinstance(self.add_vulnerability_id_to_jira_label, Unset)
            else (None, str(self.add_vulnerability_id_to_jira_label).encode(), "text/plain")
        )
        enable_github = (
            self.enable_github
            if isinstance(self.enable_github, Unset)
            else (None, str(self.enable_github).encode(), "text/plain")
        )
        enable_slack_notifications = (
            self.enable_slack_notifications
            if isinstance(self.enable_slack_notifications, Unset)
            else (None, str(self.enable_slack_notifications).encode(), "text/plain")
        )
        slack_channel = (
            self.slack_channel
            if isinstance(self.slack_channel, Unset)
            else (None, str(self.slack_channel).encode(), "text/plain")
        )
        slack_token = (
            self.slack_token
            if isinstance(self.slack_token, Unset)
            else (None, str(self.slack_token).encode(), "text/plain")
        )
        slack_username = (
            self.slack_username
            if isinstance(self.slack_username, Unset)
            else (None, str(self.slack_username).encode(), "text/plain")
        )
        enable_msteams_notifications = (
            self.enable_msteams_notifications
            if isinstance(self.enable_msteams_notifications, Unset)
            else (None, str(self.enable_msteams_notifications).encode(), "text/plain")
        )
        msteams_url = (
            self.msteams_url
            if isinstance(self.msteams_url, Unset)
            else (None, str(self.msteams_url).encode(), "text/plain")
        )
        enable_mail_notifications = (
            self.enable_mail_notifications
            if isinstance(self.enable_mail_notifications, Unset)
            else (None, str(self.enable_mail_notifications).encode(), "text/plain")
        )
        mail_notifications_to = (
            self.mail_notifications_to
            if isinstance(self.mail_notifications_to, Unset)
            else (None, str(self.mail_notifications_to).encode(), "text/plain")
        )
        false_positive_history = (
            self.false_positive_history
            if isinstance(self.false_positive_history, Unset)
            else (None, str(self.false_positive_history).encode(), "text/plain")
        )
        retroactive_false_positive_history = (
            self.retroactive_false_positive_history
            if isinstance(self.retroactive_false_positive_history, Unset)
            else (None, str(self.retroactive_false_positive_history).encode(), "text/plain")
        )
        url_prefix = (
            self.url_prefix
            if isinstance(self.url_prefix, Unset)
            else (None, str(self.url_prefix).encode(), "text/plain")
        )
        team_name = (
            self.team_name if isinstance(self.team_name, Unset) else (None, str(self.team_name).encode(), "text/plain")
        )
        time_zone: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = (None, str(self.time_zone.value).encode(), "text/plain")

        enable_product_grade = (
            self.enable_product_grade
            if isinstance(self.enable_product_grade, Unset)
            else (None, str(self.enable_product_grade).encode(), "text/plain")
        )
        product_grade = (
            self.product_grade
            if isinstance(self.product_grade, Unset)
            else (None, str(self.product_grade).encode(), "text/plain")
        )
        product_grade_a = (
            self.product_grade_a
            if isinstance(self.product_grade_a, Unset)
            else (None, str(self.product_grade_a).encode(), "text/plain")
        )
        product_grade_b = (
            self.product_grade_b
            if isinstance(self.product_grade_b, Unset)
            else (None, str(self.product_grade_b).encode(), "text/plain")
        )
        product_grade_c = (
            self.product_grade_c
            if isinstance(self.product_grade_c, Unset)
            else (None, str(self.product_grade_c).encode(), "text/plain")
        )
        product_grade_d = (
            self.product_grade_d
            if isinstance(self.product_grade_d, Unset)
            else (None, str(self.product_grade_d).encode(), "text/plain")
        )
        product_grade_f = (
            self.product_grade_f
            if isinstance(self.product_grade_f, Unset)
            else (None, str(self.product_grade_f).encode(), "text/plain")
        )
        enable_product_tag_inheritance = (
            self.enable_product_tag_inheritance
            if isinstance(self.enable_product_tag_inheritance, Unset)
            else (None, str(self.enable_product_tag_inheritance).encode(), "text/plain")
        )
        enable_benchmark = (
            self.enable_benchmark
            if isinstance(self.enable_benchmark, Unset)
            else (None, str(self.enable_benchmark).encode(), "text/plain")
        )
        enable_template_match = (
            self.enable_template_match
            if isinstance(self.enable_template_match, Unset)
            else (None, str(self.enable_template_match).encode(), "text/plain")
        )
        engagement_auto_close = (
            self.engagement_auto_close
            if isinstance(self.engagement_auto_close, Unset)
            else (None, str(self.engagement_auto_close).encode(), "text/plain")
        )
        engagement_auto_close_days = (
            self.engagement_auto_close_days
            if isinstance(self.engagement_auto_close_days, Unset)
            else (None, str(self.engagement_auto_close_days).encode(), "text/plain")
        )
        enable_finding_sla = (
            self.enable_finding_sla
            if isinstance(self.enable_finding_sla, Unset)
            else (None, str(self.enable_finding_sla).encode(), "text/plain")
        )
        enable_notify_sla_active = (
            self.enable_notify_sla_active
            if isinstance(self.enable_notify_sla_active, Unset)
            else (None, str(self.enable_notify_sla_active).encode(), "text/plain")
        )
        enable_notify_sla_active_verified = (
            self.enable_notify_sla_active_verified
            if isinstance(self.enable_notify_sla_active_verified, Unset)
            else (None, str(self.enable_notify_sla_active_verified).encode(), "text/plain")
        )
        enable_notify_sla_jira_only = (
            self.enable_notify_sla_jira_only
            if isinstance(self.enable_notify_sla_jira_only, Unset)
            else (None, str(self.enable_notify_sla_jira_only).encode(), "text/plain")
        )
        enable_notify_sla_exponential_backoff = (
            self.enable_notify_sla_exponential_backoff
            if isinstance(self.enable_notify_sla_exponential_backoff, Unset)
            else (None, str(self.enable_notify_sla_exponential_backoff).encode(), "text/plain")
        )
        allow_anonymous_survey_repsonse = (
            self.allow_anonymous_survey_repsonse
            if isinstance(self.allow_anonymous_survey_repsonse, Unset)
            else (None, str(self.allow_anonymous_survey_repsonse).encode(), "text/plain")
        )
        credentials = (
            self.credentials
            if isinstance(self.credentials, Unset)
            else (None, str(self.credentials).encode(), "text/plain")
        )
        disclaimer = (
            self.disclaimer
            if isinstance(self.disclaimer, Unset)
            else (None, str(self.disclaimer).encode(), "text/plain")
        )
        risk_acceptance_form_default_days = (
            self.risk_acceptance_form_default_days
            if isinstance(self.risk_acceptance_form_default_days, Unset)
            else (None, str(self.risk_acceptance_form_default_days).encode(), "text/plain")
        )
        risk_acceptance_notify_before_expiration = (
            self.risk_acceptance_notify_before_expiration
            if isinstance(self.risk_acceptance_notify_before_expiration, Unset)
            else (None, str(self.risk_acceptance_notify_before_expiration).encode(), "text/plain")
        )
        enable_credentials = (
            self.enable_credentials
            if isinstance(self.enable_credentials, Unset)
            else (None, str(self.enable_credentials).encode(), "text/plain")
        )
        enable_questionnaires = (
            self.enable_questionnaires
            if isinstance(self.enable_questionnaires, Unset)
            else (None, str(self.enable_questionnaires).encode(), "text/plain")
        )
        enable_checklists = (
            self.enable_checklists
            if isinstance(self.enable_checklists, Unset)
            else (None, str(self.enable_checklists).encode(), "text/plain")
        )
        enable_endpoint_metadata_import = (
            self.enable_endpoint_metadata_import
            if isinstance(self.enable_endpoint_metadata_import, Unset)
            else (None, str(self.enable_endpoint_metadata_import).encode(), "text/plain")
        )
        enable_user_profile_editable = (
            self.enable_user_profile_editable
            if isinstance(self.enable_user_profile_editable, Unset)
            else (None, str(self.enable_user_profile_editable).encode(), "text/plain")
        )
        enable_product_tracking_files = (
            self.enable_product_tracking_files
            if isinstance(self.enable_product_tracking_files, Unset)
            else (None, str(self.enable_product_tracking_files).encode(), "text/plain")
        )
        enable_finding_groups = (
            self.enable_finding_groups
            if isinstance(self.enable_finding_groups, Unset)
            else (None, str(self.enable_finding_groups).encode(), "text/plain")
        )
        enable_calendar = (
            self.enable_calendar
            if isinstance(self.enable_calendar, Unset)
            else (None, str(self.enable_calendar).encode(), "text/plain")
        )
        default_group_email_pattern = (
            self.default_group_email_pattern
            if isinstance(self.default_group_email_pattern, Unset)
            else (None, str(self.default_group_email_pattern).encode(), "text/plain")
        )
        minimum_password_length = (
            self.minimum_password_length
            if isinstance(self.minimum_password_length, Unset)
            else (None, str(self.minimum_password_length).encode(), "text/plain")
        )
        maximum_password_length = (
            self.maximum_password_length
            if isinstance(self.maximum_password_length, Unset)
            else (None, str(self.maximum_password_length).encode(), "text/plain")
        )
        number_character_required = (
            self.number_character_required
            if isinstance(self.number_character_required, Unset)
            else (None, str(self.number_character_required).encode(), "text/plain")
        )
        special_character_required = (
            self.special_character_required
            if isinstance(self.special_character_required, Unset)
            else (None, str(self.special_character_required).encode(), "text/plain")
        )
        lowercase_character_required = (
            self.lowercase_character_required
            if isinstance(self.lowercase_character_required, Unset)
            else (None, str(self.lowercase_character_required).encode(), "text/plain")
        )
        uppercase_character_required = (
            self.uppercase_character_required
            if isinstance(self.uppercase_character_required, Unset)
            else (None, str(self.uppercase_character_required).encode(), "text/plain")
        )
        non_common_password_required = (
            self.non_common_password_required
            if isinstance(self.non_common_password_required, Unset)
            else (None, str(self.non_common_password_required).encode(), "text/plain")
        )
        default_group = (
            self.default_group
            if isinstance(self.default_group, Unset)
            else (None, str(self.default_group).encode(), "text/plain")
        )
        default_group_role = (
            self.default_group_role
            if isinstance(self.default_group_role, Unset)
            else (None, str(self.default_group_role).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if enable_auditlog is not UNSET:
            field_dict["enable_auditlog"] = enable_auditlog
        if enable_deduplication is not UNSET:
            field_dict["enable_deduplication"] = enable_deduplication
        if delete_duplicates is not UNSET:
            field_dict["delete_duplicates"] = delete_duplicates
        if max_dupes is not UNSET:
            field_dict["max_dupes"] = max_dupes
        if email_from is not UNSET:
            field_dict["email_from"] = email_from
        if enable_jira is not UNSET:
            field_dict["enable_jira"] = enable_jira
        if enable_jira_web_hook is not UNSET:
            field_dict["enable_jira_web_hook"] = enable_jira_web_hook
        if disable_jira_webhook_secret is not UNSET:
            field_dict["disable_jira_webhook_secret"] = disable_jira_webhook_secret
        if jira_webhook_secret is not UNSET:
            field_dict["jira_webhook_secret"] = jira_webhook_secret
        if jira_minimum_severity is not UNSET:
            field_dict["jira_minimum_severity"] = jira_minimum_severity
        if jira_labels is not UNSET:
            field_dict["jira_labels"] = jira_labels
        if add_vulnerability_id_to_jira_label is not UNSET:
            field_dict["add_vulnerability_id_to_jira_label"] = add_vulnerability_id_to_jira_label
        if enable_github is not UNSET:
            field_dict["enable_github"] = enable_github
        if enable_slack_notifications is not UNSET:
            field_dict["enable_slack_notifications"] = enable_slack_notifications
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel
        if slack_token is not UNSET:
            field_dict["slack_token"] = slack_token
        if slack_username is not UNSET:
            field_dict["slack_username"] = slack_username
        if enable_msteams_notifications is not UNSET:
            field_dict["enable_msteams_notifications"] = enable_msteams_notifications
        if msteams_url is not UNSET:
            field_dict["msteams_url"] = msteams_url
        if enable_mail_notifications is not UNSET:
            field_dict["enable_mail_notifications"] = enable_mail_notifications
        if mail_notifications_to is not UNSET:
            field_dict["mail_notifications_to"] = mail_notifications_to
        if false_positive_history is not UNSET:
            field_dict["false_positive_history"] = false_positive_history
        if retroactive_false_positive_history is not UNSET:
            field_dict["retroactive_false_positive_history"] = retroactive_false_positive_history
        if url_prefix is not UNSET:
            field_dict["url_prefix"] = url_prefix
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if enable_product_grade is not UNSET:
            field_dict["enable_product_grade"] = enable_product_grade
        if product_grade is not UNSET:
            field_dict["product_grade"] = product_grade
        if product_grade_a is not UNSET:
            field_dict["product_grade_a"] = product_grade_a
        if product_grade_b is not UNSET:
            field_dict["product_grade_b"] = product_grade_b
        if product_grade_c is not UNSET:
            field_dict["product_grade_c"] = product_grade_c
        if product_grade_d is not UNSET:
            field_dict["product_grade_d"] = product_grade_d
        if product_grade_f is not UNSET:
            field_dict["product_grade_f"] = product_grade_f
        if enable_product_tag_inheritance is not UNSET:
            field_dict["enable_product_tag_inheritance"] = enable_product_tag_inheritance
        if enable_benchmark is not UNSET:
            field_dict["enable_benchmark"] = enable_benchmark
        if enable_template_match is not UNSET:
            field_dict["enable_template_match"] = enable_template_match
        if engagement_auto_close is not UNSET:
            field_dict["engagement_auto_close"] = engagement_auto_close
        if engagement_auto_close_days is not UNSET:
            field_dict["engagement_auto_close_days"] = engagement_auto_close_days
        if enable_finding_sla is not UNSET:
            field_dict["enable_finding_sla"] = enable_finding_sla
        if enable_notify_sla_active is not UNSET:
            field_dict["enable_notify_sla_active"] = enable_notify_sla_active
        if enable_notify_sla_active_verified is not UNSET:
            field_dict["enable_notify_sla_active_verified"] = enable_notify_sla_active_verified
        if enable_notify_sla_jira_only is not UNSET:
            field_dict["enable_notify_sla_jira_only"] = enable_notify_sla_jira_only
        if enable_notify_sla_exponential_backoff is not UNSET:
            field_dict["enable_notify_sla_exponential_backoff"] = enable_notify_sla_exponential_backoff
        if allow_anonymous_survey_repsonse is not UNSET:
            field_dict["allow_anonymous_survey_repsonse"] = allow_anonymous_survey_repsonse
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if disclaimer is not UNSET:
            field_dict["disclaimer"] = disclaimer
        if risk_acceptance_form_default_days is not UNSET:
            field_dict["risk_acceptance_form_default_days"] = risk_acceptance_form_default_days
        if risk_acceptance_notify_before_expiration is not UNSET:
            field_dict["risk_acceptance_notify_before_expiration"] = risk_acceptance_notify_before_expiration
        if enable_credentials is not UNSET:
            field_dict["enable_credentials"] = enable_credentials
        if enable_questionnaires is not UNSET:
            field_dict["enable_questionnaires"] = enable_questionnaires
        if enable_checklists is not UNSET:
            field_dict["enable_checklists"] = enable_checklists
        if enable_endpoint_metadata_import is not UNSET:
            field_dict["enable_endpoint_metadata_import"] = enable_endpoint_metadata_import
        if enable_user_profile_editable is not UNSET:
            field_dict["enable_user_profile_editable"] = enable_user_profile_editable
        if enable_product_tracking_files is not UNSET:
            field_dict["enable_product_tracking_files"] = enable_product_tracking_files
        if enable_finding_groups is not UNSET:
            field_dict["enable_finding_groups"] = enable_finding_groups
        if enable_calendar is not UNSET:
            field_dict["enable_calendar"] = enable_calendar
        if default_group_email_pattern is not UNSET:
            field_dict["default_group_email_pattern"] = default_group_email_pattern
        if minimum_password_length is not UNSET:
            field_dict["minimum_password_length"] = minimum_password_length
        if maximum_password_length is not UNSET:
            field_dict["maximum_password_length"] = maximum_password_length
        if number_character_required is not UNSET:
            field_dict["number_character_required"] = number_character_required
        if special_character_required is not UNSET:
            field_dict["special_character_required"] = special_character_required
        if lowercase_character_required is not UNSET:
            field_dict["lowercase_character_required"] = lowercase_character_required
        if uppercase_character_required is not UNSET:
            field_dict["uppercase_character_required"] = uppercase_character_required
        if non_common_password_required is not UNSET:
            field_dict["non_common_password_required"] = non_common_password_required
        if default_group is not UNSET:
            field_dict["default_group"] = default_group
        if default_group_role is not UNSET:
            field_dict["default_group_role"] = default_group_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_auditlog = d.pop("enable_auditlog", UNSET)

        enable_deduplication = d.pop("enable_deduplication", UNSET)

        delete_duplicates = d.pop("delete_duplicates", UNSET)

        max_dupes = d.pop("max_dupes", UNSET)

        email_from = d.pop("email_from", UNSET)

        enable_jira = d.pop("enable_jira", UNSET)

        enable_jira_web_hook = d.pop("enable_jira_web_hook", UNSET)

        disable_jira_webhook_secret = d.pop("disable_jira_webhook_secret", UNSET)

        jira_webhook_secret = d.pop("jira_webhook_secret", UNSET)

        _jira_minimum_severity = d.pop("jira_minimum_severity", UNSET)
        jira_minimum_severity: Union[Unset, None, SystemSettingsRequestJiraMinimumSeverity]
        if _jira_minimum_severity is None:
            jira_minimum_severity = None
        elif isinstance(_jira_minimum_severity, Unset):
            jira_minimum_severity = UNSET
        else:
            jira_minimum_severity = SystemSettingsRequestJiraMinimumSeverity(_jira_minimum_severity)

        jira_labels = d.pop("jira_labels", UNSET)

        add_vulnerability_id_to_jira_label = d.pop("add_vulnerability_id_to_jira_label", UNSET)

        enable_github = d.pop("enable_github", UNSET)

        enable_slack_notifications = d.pop("enable_slack_notifications", UNSET)

        slack_channel = d.pop("slack_channel", UNSET)

        slack_token = d.pop("slack_token", UNSET)

        slack_username = d.pop("slack_username", UNSET)

        enable_msteams_notifications = d.pop("enable_msteams_notifications", UNSET)

        msteams_url = d.pop("msteams_url", UNSET)

        enable_mail_notifications = d.pop("enable_mail_notifications", UNSET)

        mail_notifications_to = d.pop("mail_notifications_to", UNSET)

        false_positive_history = d.pop("false_positive_history", UNSET)

        retroactive_false_positive_history = d.pop("retroactive_false_positive_history", UNSET)

        url_prefix = d.pop("url_prefix", UNSET)

        team_name = d.pop("team_name", UNSET)

        _time_zone = d.pop("time_zone", UNSET)
        time_zone: Union[Unset, SystemSettingsRequestTimeZone]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = SystemSettingsRequestTimeZone(_time_zone)

        enable_product_grade = d.pop("enable_product_grade", UNSET)

        product_grade = d.pop("product_grade", UNSET)

        product_grade_a = d.pop("product_grade_a", UNSET)

        product_grade_b = d.pop("product_grade_b", UNSET)

        product_grade_c = d.pop("product_grade_c", UNSET)

        product_grade_d = d.pop("product_grade_d", UNSET)

        product_grade_f = d.pop("product_grade_f", UNSET)

        enable_product_tag_inheritance = d.pop("enable_product_tag_inheritance", UNSET)

        enable_benchmark = d.pop("enable_benchmark", UNSET)

        enable_template_match = d.pop("enable_template_match", UNSET)

        engagement_auto_close = d.pop("engagement_auto_close", UNSET)

        engagement_auto_close_days = d.pop("engagement_auto_close_days", UNSET)

        enable_finding_sla = d.pop("enable_finding_sla", UNSET)

        enable_notify_sla_active = d.pop("enable_notify_sla_active", UNSET)

        enable_notify_sla_active_verified = d.pop("enable_notify_sla_active_verified", UNSET)

        enable_notify_sla_jira_only = d.pop("enable_notify_sla_jira_only", UNSET)

        enable_notify_sla_exponential_backoff = d.pop("enable_notify_sla_exponential_backoff", UNSET)

        allow_anonymous_survey_repsonse = d.pop("allow_anonymous_survey_repsonse", UNSET)

        credentials = d.pop("credentials", UNSET)

        disclaimer = d.pop("disclaimer", UNSET)

        risk_acceptance_form_default_days = d.pop("risk_acceptance_form_default_days", UNSET)

        risk_acceptance_notify_before_expiration = d.pop("risk_acceptance_notify_before_expiration", UNSET)

        enable_credentials = d.pop("enable_credentials", UNSET)

        enable_questionnaires = d.pop("enable_questionnaires", UNSET)

        enable_checklists = d.pop("enable_checklists", UNSET)

        enable_endpoint_metadata_import = d.pop("enable_endpoint_metadata_import", UNSET)

        enable_user_profile_editable = d.pop("enable_user_profile_editable", UNSET)

        enable_product_tracking_files = d.pop("enable_product_tracking_files", UNSET)

        enable_finding_groups = d.pop("enable_finding_groups", UNSET)

        enable_calendar = d.pop("enable_calendar", UNSET)

        default_group_email_pattern = d.pop("default_group_email_pattern", UNSET)

        minimum_password_length = d.pop("minimum_password_length", UNSET)

        maximum_password_length = d.pop("maximum_password_length", UNSET)

        number_character_required = d.pop("number_character_required", UNSET)

        special_character_required = d.pop("special_character_required", UNSET)

        lowercase_character_required = d.pop("lowercase_character_required", UNSET)

        uppercase_character_required = d.pop("uppercase_character_required", UNSET)

        non_common_password_required = d.pop("non_common_password_required", UNSET)

        default_group = d.pop("default_group", UNSET)

        default_group_role = d.pop("default_group_role", UNSET)

        system_settings_request = cls(
            enable_auditlog=enable_auditlog,
            enable_deduplication=enable_deduplication,
            delete_duplicates=delete_duplicates,
            max_dupes=max_dupes,
            email_from=email_from,
            enable_jira=enable_jira,
            enable_jira_web_hook=enable_jira_web_hook,
            disable_jira_webhook_secret=disable_jira_webhook_secret,
            jira_webhook_secret=jira_webhook_secret,
            jira_minimum_severity=jira_minimum_severity,
            jira_labels=jira_labels,
            add_vulnerability_id_to_jira_label=add_vulnerability_id_to_jira_label,
            enable_github=enable_github,
            enable_slack_notifications=enable_slack_notifications,
            slack_channel=slack_channel,
            slack_token=slack_token,
            slack_username=slack_username,
            enable_msteams_notifications=enable_msteams_notifications,
            msteams_url=msteams_url,
            enable_mail_notifications=enable_mail_notifications,
            mail_notifications_to=mail_notifications_to,
            false_positive_history=false_positive_history,
            retroactive_false_positive_history=retroactive_false_positive_history,
            url_prefix=url_prefix,
            team_name=team_name,
            time_zone=time_zone,
            enable_product_grade=enable_product_grade,
            product_grade=product_grade,
            product_grade_a=product_grade_a,
            product_grade_b=product_grade_b,
            product_grade_c=product_grade_c,
            product_grade_d=product_grade_d,
            product_grade_f=product_grade_f,
            enable_product_tag_inheritance=enable_product_tag_inheritance,
            enable_benchmark=enable_benchmark,
            enable_template_match=enable_template_match,
            engagement_auto_close=engagement_auto_close,
            engagement_auto_close_days=engagement_auto_close_days,
            enable_finding_sla=enable_finding_sla,
            enable_notify_sla_active=enable_notify_sla_active,
            enable_notify_sla_active_verified=enable_notify_sla_active_verified,
            enable_notify_sla_jira_only=enable_notify_sla_jira_only,
            enable_notify_sla_exponential_backoff=enable_notify_sla_exponential_backoff,
            allow_anonymous_survey_repsonse=allow_anonymous_survey_repsonse,
            credentials=credentials,
            disclaimer=disclaimer,
            risk_acceptance_form_default_days=risk_acceptance_form_default_days,
            risk_acceptance_notify_before_expiration=risk_acceptance_notify_before_expiration,
            enable_credentials=enable_credentials,
            enable_questionnaires=enable_questionnaires,
            enable_checklists=enable_checklists,
            enable_endpoint_metadata_import=enable_endpoint_metadata_import,
            enable_user_profile_editable=enable_user_profile_editable,
            enable_product_tracking_files=enable_product_tracking_files,
            enable_finding_groups=enable_finding_groups,
            enable_calendar=enable_calendar,
            default_group_email_pattern=default_group_email_pattern,
            minimum_password_length=minimum_password_length,
            maximum_password_length=maximum_password_length,
            number_character_required=number_character_required,
            special_character_required=special_character_required,
            lowercase_character_required=lowercase_character_required,
            uppercase_character_required=uppercase_character_required,
            non_common_password_required=non_common_password_required,
            default_group=default_group,
            default_group_role=default_group_role,
        )

        system_settings_request.additional_properties = d
        return system_settings_request

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
