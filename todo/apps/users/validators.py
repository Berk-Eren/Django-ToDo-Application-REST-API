from rest_framework import serializers


def checkPasswordsAreIncludedAndEqual(
    initial_data, passwords={"password1": "password", "password2": "password2"}
):
    if (
        passwords["password1"] not in initial_data
        and passwords["password2"] not in initial_data
    ):
        raise serializers.ValidationError(
            "'%(password)s' and '%(password2)s' should be included together."
            % {"password": passwords["password1"], "password2": passwords["password2"]}
        )
    elif passwords["password1"] not in initial_data:
        raise serializers.ValidationError(
            "'%(password)s' should be included inside of the initial_data."
            % {"password": passwords["password1"]}
        )
    elif passwords["password2"] not in initial_data:
        raise serializers.ValidationError(
            "'%(password2)s' should be included inside of the initial_data."
            % {"password2": passwords["password"]}
        )
    elif initial_data[passwords["password1"]] != initial_data[passwords["password2"]]:
        raise serializers.ValidationError(
            "'%(password)s' and '%(password2)s' should be equal to each other."
            % {"password": passwords["password1"], "password2": passwords["password2"]}
        )


def checkPasswordsAreAEqualIfExist(
    initial_data, passwords={"password1": "password", "password2": "password2"}
):
    if (passwords["password1"] in initial_data) ^ (
        passwords["password2"] in initial_data
    ):
        raise serializers.ValidationError(
            "'%(password)s' and '%(password2)s' should be included together."
            % {"password": passwords["password1"], "password2": passwords["password2"]}
        )
    elif (passwords["password1"] in initial_data) and (
        passwords["password2"] in initial_data
    ):
        if initial_data[passwords["password1"]] != initial_data[passwords["password2"]]:
            raise serializers.ValidationError(
                "'%(password)s' and '%(password2)s' should be equal to each other."
                % {
                    "password": passwords["password1"],
                    "password2": passwords["password2"],
                }
            )
