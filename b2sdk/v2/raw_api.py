######################################################################
#
# File: b2sdk/v2/raw_api.py
#
# Copyright 2023 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################
from __future__ import annotations

from b2sdk import _v3 as v3
from b2sdk.raw_api import *  # noqa
from b2sdk.v2._compat import _file_infos_rename


class _OldRawAPI:
    """RawAPI compatibility layer"""

    @_file_infos_rename
    @classmethod
    def get_upload_file_headers(
        cls,
        upload_auth_token: str,
        file_name: str,
        content_length: int,
        content_type: str,
        content_sha1: str,
        file_info: dict,
        server_side_encryption: EncryptionSetting | None,
        file_retention: FileRetentionSetting | None,
        legal_hold: LegalHold | None,
        custom_upload_timestamp: int | None = None,
        cache_control: str | None = None,
    ) -> dict:
        return super().get_upload_file_headers(
            upload_auth_token=upload_auth_token,
            file_name=file_name,
            content_length=content_length,
            content_type=content_type,
            content_sha1=content_sha1,
            file_info=file_info,
            server_side_encryption=server_side_encryption,
            file_retention=file_retention,
            legal_hold=legal_hold,
            custom_upload_timestamp=custom_upload_timestamp,
            cache_control=cache_control,
        )

    @_file_infos_rename
    def upload_file(
        self,
        upload_url,
        upload_auth_token,
        file_name,
        content_length,
        content_type,
        content_sha1,
        file_info: dict,
        data_stream,
        server_side_encryption: EncryptionSetting | None = None,
        file_retention: FileRetentionSetting | None = None,
        legal_hold: LegalHold | None = None,
        custom_upload_timestamp: int | None = None,
        cache_control: str | None = None,
    ):
        return super().upload_file(
            upload_url=upload_url,
            upload_auth_token=upload_auth_token,
            file_name=file_name,
            content_length=content_length,
            content_type=content_type,
            content_sha1=content_sha1,
            file_info=file_info,
            data_stream=data_stream,
            server_side_encryption=server_side_encryption,
            file_retention=file_retention,
            legal_hold=legal_hold,
            custom_upload_timestamp=custom_upload_timestamp,
            cache_control=cache_control,
        )


class AbstractRawApi(_OldRawAPI, v3.AbstractRawApi):
    pass


class B2RawHTTPApi(_OldRawAPI, v3.B2RawHTTPApi):
    pass
