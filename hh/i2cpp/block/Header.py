from .Basic import Basic
from .String_Length_Data import String_Length_Data
from .String_Content_Data import String_Content_Data


class Header(Basic):
    def __init__(self):
        self.magic = 0
        self.version = 0
        self.strings_length_offset = 0
        self.strings_length_content_size = 0
        self.string_length_data = None

        self.strings_content_offset = 0  # 字符串偏移量起始
        self.strings_content_size = 0  # 字符串偏移量大小
        self.string_data = []

        self.other = None

    def decode(self):
        self.magic = self.read_int_32()
        self.version = self.read_int_32()

        self.strings_length_offset = self.read_int_32()  # 字符串偏移量起始
        self.strings_length_content_size = self.read_int_32()  # 字符串偏移量大小

        self.strings_content_offset = self.read_int_32()
        self.strings_content_size = self.read_int_32()

        self.other = [[self.read_int_32(), self.read_int_32()] for i in range((self.strings_length_offset // 4 - 6) // 2)]
        print(self.other)
        # self.stringOffset = self.read_int_32()  # string data for metadata
        # self.stringCount = self.read_int_32()  #
        # self.eventsOffset = self.read_int_32()  # Il2CppEventDefinition
        # self.eventsCount = self.read_int_32()  #
        # self.propertiesOffset = self.read_int_32()  # Il2CppPropertyDefinition
        # self.propertiesCount = self.read_int_32()  #
        # self.methodsOffset = self.read_int_32()  # Il2CppMethodDefinition
        # self.methodsCount = self.read_int_32()  #
        # self.parameterDefaultValuesOffset = self.read_int_32()  # Il2CppParameterDefaultValue
        # self.parameterDefaultValuesCount = self.read_int_32()  #
        # self.fieldDefaultValuesOffset = self.read_int_32()  # Il2CppFieldDefaultValue
        # self.fieldDefaultValuesCount = self.read_int_32()  #
        # self.fieldAndParameterDefaultValueDataOffset = self.read_int_32()  # uint8_t
        # self.fieldAndParameterDefaultValueDataCount = self.read_int_32()  #
        # self.fieldMarshaledSizesOffset = self.read_int_32()  # Il2CppFieldMarshaledSize
        # self.fieldMarshaledSizesCount = self.read_int_32()  #
        # self.parametersOffset = self.read_int_32()  # Il2CppParameterDefinition
        # self.parametersCount = self.read_int_32()  #
        # self.fieldsOffset = self.read_int_32()  # Il2CppFieldDefinition
        # self.fieldsCount = self.read_int_32()  #
        # self.genericParametersOffset = self.read_int_32()  # Il2CppGenericParameter
        # self.genericParametersCount = self.read_int_32()  #
        # self.genericParameterConstraintsOffset = self.read_int_32()  # TypeIndex
        # self.genericParameterConstraintsCount = self.read_int_32()  #
        # self.genericContainersOffset = self.read_int_32()  # Il2CppGenericContainer
        # self.genericContainersCount = self.read_int_32()  #
        # self.nestedTypesOffset = self.read_int_32()  # TypeDefinitionIndex
        # self.nestedTypesCount = self.read_int_32()  #
        # self.interfacesOffset = self.read_int_32()  # TypeIndex
        # self.interfacesCount = self.read_int_32()  #
        # self.vtableMethodsOffset = self.read_int_32()  # EncodedMethodIndex
        # self.vtableMethodsCount = self.read_int_32()  #
        # self.interfaceOffsetsOffset = self.read_int_32()  # Il2CppInterfaceOffsetPair
        # self.interfaceOffsetsCount = self.read_int_32()  #
        # self.typeDefinitionsOffset = self.read_int_32()  # Il2CppTypeDefinition
        # self.typeDefinitionsCount = self.read_int_32()  #
        # self.rgctxEntriesOffset = self.read_int_32()  # Il2CppRGCTXDefinition
        # self.rgctxEntriesCount = self.read_int_32()  #
        # self.imagesOffset = self.read_int_32()  # Il2CppImageDefinition
        # self.imagesCount = self.read_int_32()  #
        # self.assembliesOffset = self.read_int_32()  # Il2CppAssemblyDefinition
        # self.assembliesCount = self.read_int_32()  #
        # self.metadataUsageListsOffset = self.read_int_32()  # Il2CppMetadataUsageList
        # self.metadataUsageListsCount = self.read_int_32()  #
        # self.metadataUsagePairsOffset = self.read_int_32()  # Il2CppMetadataUsagePair
        # self.metadataUsagePairsCount = self.read_int_32()  #
        # self.fieldRefsOffset = self.read_int_32()  # Il2CppFieldRef
        # self.fieldRefsCount = self.read_int_32()  #
        # self.referencedAssembliesOffset = self.read_int_32()  # int32_t
        # self.referencedAssembliesCount = self.read_int_32()  #
        # self.attributesInfoOffset = self.read_int_32()  # Il2CppCustomAttributeTypeRange
        # self.attributesInfoCount = self.read_int_32()  #
        # self.attributeTypesOffset = self.read_int_32()  # TypeIndex
        # self.attributeTypesCount = self.read_int_32()  #

        self.seek(self.strings_length_offset)
        self.string_length_data = [[self.read_int_32(), self.read_int_32()] for i in range(self.strings_length_content_size // 8)]

        self.seek(self.strings_content_offset)
        for index, i in enumerate(self.string_length_data):
            key = self.read_string(i[0])
            self.string_data.append("%d_%s" % (index, key))

    def encode(self):
        data = bytearray()
        string_length_data = bytearray()
        string_content_data = bytearray()
        offset = 0
        for index, json_key in enumerate(self.string_data):
            key = json_key[len("%d_" % index):]
            value = self.json_result.get(json_key, "")
            key_encode, value_encode = key.encode(), value.encode()
            item_length = len(value_encode) if value else len(key_encode)
            string_length_data.extend(item_length.to_bytes(4, byteorder='little'))
            string_length_data.extend(offset.to_bytes(4, byteorder='little'))
            offset += item_length
            string_content_data.extend(value_encode if value else key_encode)
        self.align_4(string_content_data)
        data.extend(string_length_data)
        data.extend(string_content_data)
        self.read_f.seek(self.strings_content_offset + self.strings_content_size)
        data.extend(self.read_f.read())

        string_content_length = len(string_content_data)

        self.write_int_32(self.magic)
        self.write_int_32(self.version)
        self.write_int_32(self.strings_length_offset)
        self.write_int_32(self.strings_length_content_size)
        self.write_int_32(self.strings_content_offset)
        self.write_int_32(string_content_length)

        sub = self.strings_content_size - string_content_length
        for item in self.other:
            self.write_int_32(item[0] - sub)
            self.write_int_32(item[1])
        self.write_f.write(data)
