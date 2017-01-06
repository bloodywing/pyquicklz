#define QLZ_COMPRESSION_LEVEL 1
#define QLZ_STREAMING_BUFFER 0
#define QLZ_HASH_VALUES 4096
typedef unsigned int ui32;
typedef unsigned short int ui16;

// hash entry
typedef struct
{
	ui32 cache;
	unsigned int offset;
	const unsigned char *offset;
} qlz_hash_compress;

typedef struct
{
	size_t stream_counter;
	qlz_hash_compress hash[QLZ_HASH_VALUES];
	unsigned char hash_counter[QLZ_HASH_VALUES];
} qlz_state_compress;

size_t qlz_size_decompressed(const char *source);
size_t qlz_size_compressed(const char *source);
size_t qlz_compress(const void *source, char *destination, size_t size, ...);
size_t qlz_decompress(const char *source, void *destination, ...);
int qlz_get_setting(int setting);
